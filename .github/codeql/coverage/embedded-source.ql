/**
 * Source-extraction inventory only; does not replace or filter security queries.
 */
import javascript

string sourceKind(TopLevel top) {
  top instanceof InlineScript and result = "inline-script"
  or
  top instanceof EventHandlerCode and result = "event-handler"
  or
  top instanceof JavaScriptURL and result = "javascript-url"
}

string minification(TopLevel top) {
  top.isMinified() and result = "true"
  or
  not top.isMinified() and result = "false"
}

from TopLevel top
select top.getFile().getRelativePath(), sourceKind(top),
  top.getLocation().getStartLine(), top.getLocation().getStartColumn(),
  top.getNumberOfLinesOfCode(), minification(top)
