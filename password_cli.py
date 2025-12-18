#!/usr/bin/env python3

import argparse
import string
from password_core import generate_password


def main():
    parser = argparse.ArgumentParser(description="Secure password generator")

    parser.add_argument("--min-length", type=int, default=15)
    parser.add_argument("--max-length", type=int, default=30)

    parser.add_argument("--alphabet", type=str,
                        default=string.ascii_letters + string.digits)
    parser.add_argument("--special-chars", type=str,
                        default="!@#$%^&*()_+=-`~.,")

    parser.add_argument("--no-upper", action="store_false", dest="upper")
    parser.add_argument("--no-lower", action="store_false", dest="lower")
    parser.add_argument("--no-digit", action="store_false", dest="digit")
    parser.add_argument("--no-special", action="store_true")
    parser.add_argument("--no-clipboard", action="store_false",
                        dest="copy_to_clipboard")

    parser.set_defaults(
        upper=True,
        lower=True,
        digit=True,
        copy_to_clipboard=True
    )

    args = parser.parse_args()

    special_chars = "" if args.no_special else args.special_chars

    password = generate_password(
        alphabet=args.alphabet,
        special_chars=special_chars,
        minimum_length=args.min_length,
        maximum_length=args.max_length,
        copy_to_clipboard=args.copy_to_clipboard,
        upper=args.upper,
        lower=args.lower,
        digit=args.digit,
    )

    print(password)

if __name__ == "__main__":
    main()
