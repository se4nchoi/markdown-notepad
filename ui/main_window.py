"""Main application window with editor and live preview."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter

from core.markdown_renderer import render_markdown_to_html
from ui.editor import MarkdownEditor
from ui.preview import PreviewPane
from ui.theme import apply_editor_theme, apply_preview_theme, is_dark_mode

SAMPLE_MARKDOWN = """# Welcome to Markdown Notepad

Start typing on the **left** to see a live preview on the *right*.

## Features (coming soon)

- File open and save
- Syntax highlighting
- Themes

## Example list

1. Write Markdown
2. See instant preview
3. Build incrementally

> This is a blockquote. Edit this text to try it out.

Inline `code` and fenced blocks:

```
def greet(name: str) -> str:
    return f"Hello, {name}!"
```
"""


class MainWindow(QMainWindow):
    """
    Hosts the editor and preview panes in a horizontal splitter.

    Coordinates UI layout and wires the editor's textChanged signal to
    refresh the preview. Does not perform Markdown parsing itself.
    """

    def __init__(self) -> None:
        super().__init__()
        self._editor = MarkdownEditor()
        self._preview = PreviewPane()

        self._setup_window()
        self._setup_layout()
        self._connect_signals()
        self._apply_theme()
        self._load_sample_content()

    def _setup_window(self) -> None:
        self.setWindowTitle("Markdown Notepad")
        self.resize(1200, 700)

    def _setup_layout(self) -> None:
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self._editor)
        splitter.addWidget(self._preview)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([600, 600])

        self.setCentralWidget(splitter)

    def _connect_signals(self) -> None:
        self._editor.textChanged.connect(self._update_preview)
        QApplication.styleHints().colorSchemeChanged.connect(self._apply_theme)

    def _load_sample_content(self) -> None:
        self._editor.setPlainText(SAMPLE_MARKDOWN)
        self._update_preview()

    def _apply_theme(self) -> None:
        dark = is_dark_mode()
        apply_editor_theme(self._editor, dark_mode=dark)
        apply_preview_theme(self._preview, dark_mode=dark)
        self._update_preview()

    def _update_preview(self) -> None:
        markdown_text = self._editor.toPlainText()
        html = render_markdown_to_html(markdown_text, dark_mode=is_dark_mode())
        self._preview.set_html(html)
