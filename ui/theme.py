"""Detect system color scheme and apply matching widget styles."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTextBrowser, QTextEdit


def is_dark_mode() -> bool:
    """
    Return True when the OS/Qt color scheme is dark.

    Falls back to palette luminance when the scheme is unknown.
    """
    scheme = QApplication.styleHints().colorScheme()
    if scheme == Qt.ColorScheme.Dark:
        return True
    if scheme == Qt.ColorScheme.Light:
        return False

    return QApplication.palette().window().color().lightness() < 128


def apply_editor_theme(editor: QTextEdit, *, dark_mode: bool) -> None:
    """Apply light or dark styling to the Markdown editor."""
    if dark_mode:
        editor.setStyleSheet(
            "QTextEdit {"
            "  background-color: #1e1e1e;"
            "  color: #e0e0e0;"
            "  border: none;"
            "  selection-background-color: #264f78;"
            "}"
        )
    else:
        editor.setStyleSheet(
            "QTextEdit {"
            "  background-color: #ffffff;"
            "  color: #333333;"
            "  border: none;"
            "  selection-background-color: #cce5ff;"
            "}"
        )


def apply_preview_theme(preview: QTextBrowser, *, dark_mode: bool) -> None:
    """Apply light or dark styling to the preview pane chrome."""
    if dark_mode:
        preview.setStyleSheet(
            "QTextBrowser {"
            "  background-color: #1e1e1e;"
            "  color: #e0e0e0;"
            "  border: none;"
            "}"
        )
    else:
        preview.setStyleSheet(
            "QTextBrowser {"
            "  background-color: #ffffff;"
            "  color: #333333;"
            "  border: none;"
            "}"
        )
