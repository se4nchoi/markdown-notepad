"""Markdown source editor widget."""

from PySide6.QtWidgets import QTextEdit


class MarkdownEditor(QTextEdit):
    """
    A plain-text editing surface for writing Markdown.

    Subclasses QTextEdit to provide a dedicated editor widget while keeping
    all Markdown-specific behavior (such as live preview updates) in MainWindow.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setPlaceholderText("Write Markdown here...")
        self.setTabStopDistance(40)
