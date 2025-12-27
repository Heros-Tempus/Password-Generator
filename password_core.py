#!/usr/bin/env python3

import pyperclip
import secrets
import string


def generate_password(
    alphabet: str = string.ascii_letters + string.digits,
    special_chars: str = "!@#$%^&*()_+=-`~.,",
    minimum_length: int = 15,
    maximum_length: int = 30,
    copy_to_clipboard: bool = True,
    upper: bool = True,
    lower: bool = True,
    digit: bool = True
) -> str:
    """
    Generate a secure password meeting specified criteria.
    
    Parameters:
        alphabet (str): The characters allowed in the password.
        special_chars (str): A string of special characters to include in the password.
        minimum_length (int): The minimum length of the password.
        maximum_length (int): The maximum length of the password.
        copy_to_clipboard (bool): If True, copies the generated password to the clipboard.
        upper (bool): If True, the password must contain at least one uppercase letter.
        lower (bool): If True, the password must contain at least one lowercase letter.
        digit (bool): If True, the password must contain at least one digit.
        
    Returns:
        str: A randomly generated password meeting all criteria.
    """
    
    criteria = []
    if upper:
        criteria.append(lambda s: any(c.isupper() for c in s))  # has uppercase
    if lower:
        criteria.append(lambda s: any(c.islower() for c in s))  # has lowercase
    if digit:
        criteria.append(lambda s: any(c.isdigit() for c in s))  # has digit
    if special_chars:
        alphabet += special_chars
        criteria.append(lambda s: any(c in special_chars for c in s))  # has special character

    if minimum_length > maximum_length:
        raise ValueError("Minimum length cannot be greater than maximum length")
    if not alphabet:
        raise ValueError("Alphabet cannot be empty")
    if criteria and not all(any(criterion(c) for c in alphabet) for criterion in criteria):
        raise ValueError("Alphabet must contain characters that can satisfy each criterion")

    random_gen = secrets.SystemRandom()
    
    while True:
        length = random_gen.randint(minimum_length, maximum_length)
        password = ''.join(random_gen.choice(alphabet) for _ in range(length))
        if not criteria or all(criterion(password) for criterion in criteria):
            if copy_to_clipboard:
                pyperclip.copy(password)
            return password

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
