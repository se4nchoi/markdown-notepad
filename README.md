# Markdown Notepad

A small desktop Markdown preview app built with Python and PySide6.

Project was made to explore basic desktop GUI structure, live text updates, and Markdown-to-HTML rendering through python.

## Preview

![Markdown Notepad](docs/screenshot/markdown-notepad.png)

## Current Features

* Markdown text input
* Live rendered preview
* Resizable split-pane layout
* Support for common Markdown syntax
* Light and dark mode based on the system theme

## Development Environment

Originally developed on:

* Windows 11
* Python 3
* PySide6
* Python Markdown

I first tried running the GUI through WSL, but moved the project to a native Windows Python environment after running into display and environment issues.

## Setup

### Prerequisites

Install:

* Python 3.10 or newer
* Git

Clone the repository:

```powershell
git clone https://github.com/se4nchoi/markdown-notepad.git
cd markdown-notepad
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Run the app:

```powershell
python main.py
```

## Project Structure

```text
main.py
core/
└── markdown_renderer.py

ui/
├── editor.py
├── main_window.py
├── preview.py
└── theme.py
```

## Limitations

The current version does not include:

* File open or save
* Formatting controls
* Markdown syntax highlighting
* Export options
* Copy-to-clipboard actions
* Application packaging

The interface also follows a standard Markdown-source-to-preview layout, which is different from the original idea of a lightweight Notion-style input tool that produces reusable Markdown output.

## Development Process

This was a small AI-assisted experiment.

I defined the intended behavior, used Antigravity and Cursor for much of the implementation, reviewed the generated code, and debugged the GUI environment across WSL and Windows.

The project is best treated as an early PySide6 learning exercise rather than a finished Markdown editor.

## What I Explored

* PySide6 application structure
* Qt widgets and signal handling
* Live updates between editor and preview panes
* Markdown-to-HTML conversion
* Basic desktop theming
* Differences between GUI development in WSL and native Windows

## Possible Next Direction

A future version could reverse the current workflow:

```text
Lightweight formatted input
        ↓
Clean Markdown output
        ↓
Copy into Notion or a tracking database
```

That would be a separate iteration rather than a small extension of the current app.

## License

No license has been added yet.
