import random

import pyperclip
from constants import CHAR_TYPES_MAP


def get_available_characters(selected_char_types: list[str]) -> str:
    """
    Get a string of available characters based on the selected character types.
    
    Args:
        selected_char_types (list[str]): List of selected character type keys.
    
    Returns:
        str: A string containing all available characters for the selected types.
    """
    return ''.join(''.join(CHAR_TYPES_MAP[char_type]) for char_type in selected_char_types)


def generate_password(available_chars: str, selected_char_types: list[str], password_length: int) -> str:
    """
    Generate a password based on the available characters, ensuring at least one character of each selected type.
    
    Args:
        available_chars (str): A string of available characters.
        selected_char_types (list[str]): List of selected character type keys.
        password_length (int): The desired password length.
    
    Returns:
        str: A generated password.
    """
    password = [random.choice(CHAR_TYPES_MAP[char_type]) for char_type in selected_char_types]
    
    remaining_length = password_length - len(password)
    password += random.sample(available_chars, remaining_length)
    
    random.shuffle(password)
    
    return ''.join(password)


def copy_password_to_clipboard(password: str) -> None:
    """
    Copy the generated password to the clipboard.
    
    Args:
        password (str): The generated password.
    """
    pyperclip.copy(password)
    
    return None