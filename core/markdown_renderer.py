"""Convert Markdown source text into a styled HTML document."""

import markdown

_LIGHT_STYLES = """
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333333;
            background-color: #ffffff;
            padding: 12px;
            margin: 0;
        }
        a {
            color: #0969da;
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 1.2em;
            margin-bottom: 0.4em;
            line-height: 1.25;
        }
        p {
            margin: 0.6em 0;
        }
        code {
            background-color: #f4f4f4;
            color: #333333;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Consolas, "Courier New", monospace;
        }
        pre {
            background-color: #f4f4f4;
            color: #333333;
            padding: 12px;
            border-radius: 4px;
            overflow-x: auto;
        }
        pre code {
            background: none;
            padding: 0;
        }
        blockquote {
            border-left: 4px solid #dddddd;
            margin: 0.6em 0;
            padding-left: 12px;
            color: #666666;
        }
        ul, ol {
            padding-left: 1.5em;
        }
"""

_DARK_STYLES = """
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #e0e0e0;
            background-color: #1e1e1e;
            padding: 12px;
            margin: 0;
        }
        a {
            color: #6cb6ff;
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 1.2em;
            margin-bottom: 0.4em;
            line-height: 1.25;
            color: #f0f0f0;
        }
        p {
            margin: 0.6em 0;
        }
        code {
            background-color: #2d2d2d;
            color: #e0e0e0;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Consolas, "Courier New", monospace;
        }
        pre {
            background-color: #2d2d2d;
            color: #e0e0e0;
            padding: 12px;
            border-radius: 4px;
            overflow-x: auto;
        }
        pre code {
            background: none;
            padding: 0;
        }
        blockquote {
            border-left: 4px solid #555555;
            margin: 0.6em 0;
            padding-left: 12px;
            color: #aaaaaa;
        }
        ul, ol {
            padding-left: 1.5em;
        }
"""


def render_markdown_to_html(markdown_text: str, *, dark_mode: bool = False) -> str:
    """
    Convert Markdown text into a complete HTML document.

    Args:
        markdown_text: Raw Markdown source from the editor.
        dark_mode: When True, use a dark color scheme for the rendered HTML.

    Returns:
        A full HTML document string suitable for display in QTextBrowser.
    """
    body_html = markdown.markdown(markdown_text)
    styles = _DARK_STYLES if dark_mode else _LIGHT_STYLES

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
{styles}
    </style>
</head>
<body>
{body_html}
</body>
</html>"""
