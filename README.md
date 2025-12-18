# Password Generator

A secure, offline password generator written in Python.

This project is intentionally split into two scripts:

- **`password_core.py`** — double-click friendly, zero configuration  
  Generates a secure password and copies it directly to the clipboard.
- **`password_cli.py`** — full command-line interface  
  Allows fine-grained control over password generation using flags.

---

## Features

- Cryptographically secure randomness (`secrets.SystemRandom`)
- Configurable password length
- Optional uppercase, lowercase, digits, and special characters
- Clipboard integration via `pyperclip`

---

## Requirements

- Python **3.8+**
- `pyperclip`

Install dependencies:

```bash
pip install pyperclip
