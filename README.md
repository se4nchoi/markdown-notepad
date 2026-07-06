# Markdown Notepad

A desktop Markdown editor with live HTML preview, built with Python and PySide6.

Coded with Cursor AI.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Architecture

- `main.py` — application entry point
- `ui/main_window.py` — window layout and signal wiring
- `ui/editor.py` — Markdown source editor (`QTextEdit`)
- `ui/preview.py` — HTML preview pane (`QTextBrowser`)
- `core/markdown_renderer.py` — Markdown-to-HTML conversion
