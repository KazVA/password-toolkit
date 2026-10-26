# Password Toolkit

A Python command-line tool for generating random passwords and estimating password entropy.

## Features
- Secure random password generation using Python's `secrets` module
- Customizable password length
- Basic entropy estimation
- Simple strength ratings

## Requirements
- Python 3
- No external dependencies

## Usage

Generate a 20-character password:

```bash
python passcheck.py gen -l 20
```

Check a sample password:

```bash
python passcheck.py check "example123"
```

## Example Output

```text
YourGeneratedPassword (Excellent)
```

The generated password and rating will vary. Entropy ratings are rough estimates, not guarantees of security.