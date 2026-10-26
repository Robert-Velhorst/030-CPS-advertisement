# Inline JavaScript security and quality coverage

GitHub reports only HTML for this repository, but demo/index.html contains an
executable inline script and six event-handler attributes. Default setup has
no selected languages and rejects explicit JavaScript selection with HTTP422.
That is a language-detector limitation, not evidence that the source has no
JavaScript or that a security scan passed.

This draft prepares the documented advanced CLI route with the current stable
CodeQL2.27.3 release bundle and its publisher SHA256. It analyzes the complete
JavaScript/HTML, Python evidence helper and GitHub Actions workflow sources with
the free security-and-quality suites. This is separate from GitHub's paid Code
Quality product. No original application file, case, helper or assertion is
changed, and no source/query/severity/advisory exclusions are added.

Every tracked source input is hashed before/after analysis. The extraction
archive must retain matching bytes for each selected language's genuine source
inputs. A separate inventory query records actual inline-script and event-handler
ASTs and their minification classification; its counts must match the unchanged
HTML source. This audit query does not replace or filter security queries and
does not execute application scripts. Every raw SARIF finding is retained; any
finding at any severity fails the qualification. The workflow also preserves
all diagnostic output on failure.

Pull-request runs retain artifacts without attempting blocked SARIF uploads
while default setup is configured. After reviewed qualification, adoption needs
explicit merge approval and a coordinated switch from empty default setup to
advanced setup before main's automatic SARIF upload. No switch or main merge is
included in this draft. Initial local review is limited to source, AST, hash and
workflow inspection. Actual hosted query compilation, inline extraction and
full security/quality results remain unproved until the exact run completes.

Sources: [GitHub's setup selection](https://docs.github.com/en/code-security/concepts/code-scanning/setup-types),
[inline-script/event-handler CodeQL support](https://codeql.github.com/docs/codeql-language-guides/codeql-library-for-javascript/),
[query suites](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-query-suites),
and [the public stable CLI](https://github.com/github/codeql-cli-binaries/releases/tag/v2.27.3).
