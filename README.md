# Password Generator

A secure, offline password generator written in Python.

A simple Python password generator that creates cryptographically secure passwords **without storing them**.  
You can run it directly with default settings, or use the CLI to customize the output.

## Features

- Cryptographically secure randomness via Python's `secrets` module
- Configurable password length
- Optional uppercase, lowercase, digits, and special characters
- Optional clipboard copying
- Simple command-line interface

## Requirements

- `Python 3`
- `pyperclip`

Install the dependency with:

```bash
pip install pyperclip
```

## Usage

### Default usage

Run the core script directly to generate a password with the default settings:

```bash
python password_core.py
```

### Command-line usage

Use the CLI wrapper to customize generation options:

```bash
python password_cli.py
```

Example:

```bash
python password_cli.py --min-length 20 --max-length 24 --no-special
```

## Command-Line Options

### Length

- `--min-length`: Minimum password length (default: `15`)
- `--max-length`: Maximum password length (default: `30`)

### Character sets

- `--alphabet`: Base alphabet to generate from  
  Default: ASCII letters and digits
- `--special-chars`: Special characters to include  
  Default: ``!@#$%^&*()_+=-`~.,``

### Toggles

- `--no-upper`: Exclude uppercase letters
- `--no-lower`: Exclude lowercase letters
- `--no-digit`: Exclude digits
- `--no-special`: Exclude special characters
- `--no-clipboard`: Do not copy the generated password to the clipboard

## Examples

Generate a password without special characters:

```bash
python password_cli.py --no-special
```

Generate a password using only letters:

```bash
python password_cli.py --no-digit --no-special
```

Generate a password without copying it to the clipboard:

```bash
python password_cli.py --no-clipboard
```

## Programmatic Use

You can also import the generator from `password_core.py`:

```python
from password_core import generate_password

password = generate_password()
print(password)
```

You can customize the function directly as well:

```python
from password_core import generate_password

password = generate_password(
    minimum_length=12,
    maximum_length=20,
    copy_to_clipboard=False,
    upper=True,
    lower=True,
    digit=True,
)
print(password)
```

## Behavior

- Password length is chosen randomly between the minimum and maximum values.
- The password is regenerated until it satisfies the selected character requirements.
- If clipboard copying is enabled, the generated password is copied automatically.
- The program raises a `ValueError` if:
  - the minimum length is greater than the maximum length
  - the alphabet is empty
  - the selected alphabet cannot satisfy the enabled character requirements
