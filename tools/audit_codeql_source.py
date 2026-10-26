"""Audit scanner inputs/results on hosted workers; never run application scripts."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import csv
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import zipfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def tracked():
    names = subprocess.check_output(['git', 'ls-files', '-z']).decode().split('\0')
    result = {}
    root = Path.cwd().resolve()
    for name in names:
        if not name:
            continue
        if any(ord(char) < 32 for char in name) or not Path(name).resolve(strict=True).is_relative_to(root):
            raise RuntimeError('Every tracked input must remain inside the reviewed source root')
        if Path(name).is_file():
            result[name] = sha(Path(name).read_bytes())
    return result


class HTMLSource(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = 0
        self.events = 0
        self.javascript_urls = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'script' and attrs.get('type', '').lower() in ['', 'module', 'text/javascript', 'application/javascript', 'text/ecmascript', 'application/ecmascript']:
            self.scripts += 1
        self.events += sum(name.lower().startswith('on') for name in attrs)
        self.javascript_urls += sum(str(value).strip().lower().startswith('javascript:') for value in attrs.values() if value)


def main():
    if sys.platform != 'linux' or os.geteuid() == 0 or os.environ.get('RUNNER_ENVIRONMENT') != 'github-hosted':
        raise RuntimeError('Use only a non-root disposable GitHub-hosted worker')
    if platform.python_version() != '3.15.1':
        raise RuntimeError('Retain the current stable metadata runtime')
    if sys.flags.optimize:
        raise RuntimeError('All audit assertions must remain enabled')
    mode, destination = sys.argv[1:]
    assert mode in ['before', 'verify']
    folder = Path(destination).resolve()
    if not folder.is_relative_to(Path(os.environ['RUNNER_TEMP']).resolve()):
        raise RuntimeError('Keep evidence inside the disposable worker temporary directory')
    folder.mkdir(parents=True, exist_ok=True)
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    assert re.fullmatch('[0-9a-f]{40}', os.environ['REVIEWED_SHA']) and head == os.environ['REVIEWED_SHA']
    if mode == 'before':
        identity = {'head': head, 'tree': subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip(),
            'source_sha256': tracked(), 'metadata_python': platform.python_version(),
            'application_or_page_scripts_executed': False}
        (folder / 'source-before.json').write_text(json.dumps(identity, indent=2) + '\n')
        return
    sarif_path = folder / 'full-source.sarif'
    with Path(os.environ['GITHUB_OUTPUT']).open('a') as output:
        output.write('sarif_present=' + str(sarif_path.is_file()).lower() + '\n')
    before = json.loads((folder / 'source-before.json').read_text())
    current = tracked()
    changed = [name for name, value in before['source_sha256'].items() if current.get(name) != value]
    version = json.loads((folder / 'cli-version.json').read_text())
    assert version['version'] == os.environ['CODEQL_VERSION']
    sarif = json.loads(sarif_path.read_text())
    assert sarif['version'] == '2.1.0' and len(sarif['runs']) == 1
    run = sarif['runs'][0]
    components = [run['tool']['driver'], *run['tool'].get('extensions', [])]
    assert not any('pr-diff-range' in item.get('name', '') for item in components)
    rules = sorted({rule['id'] for item in components for rule in item.get('rules', [])})
    assert rules
    language = os.environ['LANGUAGE']
    expected = {}
    html_metadata = {}
    for name, value in current.items():
        if language == 'javascript':
            if name.endswith(('.js', '.jsx', '.mjs', '.cjs', '.ts', '.tsx')):
                expected[name] = value
            if name.endswith(('.html', '.htm', '.xhtml')):
                parsed = HTMLSource()
                parsed.feed(Path(name).read_text())
                if parsed.scripts or parsed.events or parsed.javascript_urls:
                    expected[name] = value
                    html_metadata[name] = {'inline-script': parsed.scripts, 'event-handler': parsed.events,
                        'javascript-url': parsed.javascript_urls}
        elif language == 'python' and name.endswith('.py'):
            expected[name] = value
        elif language == 'actions' and (name.startswith('.github/workflows/') and name.endswith(('.yml', '.yaml')) or name.endswith(('/action.yml', '/action.yaml'))):
            expected[name] = value
    assert expected, 'The selected language must have genuine source inputs'
    archive_verified = []
    with zipfile.ZipFile(folder / 'extracted-source.zip') as source:
        for name, value in expected.items():
            matches = [p for p in source.namelist() if p.endswith('/' + name) or p == name]
            assert len(matches) == 1, 'Source missing or ambiguous in extraction: ' + name
            assert sha(source.read(matches[0])) == value, 'Extracted source hash differs: ' + name
            archive_verified.append(name)
    coverage = []
    missing = []
    headers = []
    if language == 'javascript':
        with (folder / 'embedded-source.csv').open(newline='') as stream:
            reader = csv.reader(stream)
            headers = next(reader)
            for row in reader:
                assert len(row) == 6
                coverage.append({'path': row[0], 'kind': row[1], 'line': row[2],
                    'column': row[3], 'lines_of_code': row[4], 'minified': row[5]})
        actual = Counter((row['path'], row['kind']) for row in coverage)
        for name, kinds in html_metadata.items():
            for kind, count in kinds.items():
                if actual[name, kind] != count:
                    missing.append({'path': name, 'kind': kind, 'expected': count, 'actual': actual[name, kind]})
    findings = run.get('results', [])
    report = {'source_head': head, 'language': language, 'CLI_version': version,
        'complete_source_not_PR_diff': True, 'tracked_source_count': len(current), 'changed_tracked_inputs': changed,
        'matching_extracted_source_paths': archive_verified, 'embedded_expected_counts': html_metadata,
        'embedded_coverage_columns': headers,
        'embedded_actual_top_levels': coverage, 'embedded_coverage_mismatches': missing,
        'rules': rules, 'raw_finding_count': len(findings), 'all_raw_results_retained': True,
        'application_or_page_scripts_executed': False, 'new_application_cases_authored': False,
        'query_source_severity_or_advisory_exclusions_added': False,
        'full_application_runtime_or_security_remediation_acceptance': False}
    (folder / 'summary.json').write_text(json.dumps(report, indent=2) + '\n')
    assert not changed, 'Scanner must not modify its source inputs'
    assert not missing, 'Inline source or event-handler extraction is incomplete'
    assert not findings, 'Unfiltered CodeQL security/quality findings remain in the retained SARIF'


if __name__ == '__main__':
    main()
