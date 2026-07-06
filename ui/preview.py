"""HTML preview pane for rendered Markdown."""

from PySide6.QtWidgets import QTextBrowser


class PreviewPane(QTextBrowser):
    """
    Displays rendered Markdown as HTML.

    Subclasses QTextBrowser so the preview is read-only and uses Qt's
    built-in HTML rendering without requiring QWebEngineView.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setOpenExternalLinks(True)

    def set_html(self, html: str) -> None:
        """Load a complete HTML document into the preview pane."""
        self.setHtml(html)
