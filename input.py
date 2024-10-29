import argparse
from constants import *


def prompt_for_password_length() -> int:
    """
    Prompt the user to enter a password length within the allowed range.
    
    Returns:
        int: A valid password length within the specified range.
    """
    while True:
        try:
            length = int(input(LENGTH_MSG) or DEFAULT_PASSWORD_LENGTH)
            if MIN_PASSWORD_LENGTH <= length <= MAX_PASSWORD_LENGTH:
                return length
            else:
                print(INVALID_LENGTH_MSG)
        except ValueError:
            print(INVALID_DIGIT_MSG)


def prompt_for_password_char_types() -> list:
    """
    Prompt the user to enter the desired password char types.
    
    Returns:
        list: A list of selected char types keys in lowercase.
    """
    while True:
        default_char_types = ' '.join(CHAR_TYPES_MAP.keys())
        selected_char_types = (input(CHAR_TYPES_MSG) or default_char_types).lower().strip().split(' ')
        if all(option in CHAR_TYPES_MAP.keys() for option in selected_char_types):
            return selected_char_types
        else:
            print(INVALID_CHAR_TYPES_MSG)


def prompt_for_show_password() -> bool:
    """
    Prompt the user to decide whether to show the generated password.
    
    Returns:
        bool: True if the user wants to show the generated password, False otherwise.
    """
    while True:
        user_input = input(SHOW_PASSWORD_OPTIONS_MSG).lower().strip() or 'n'
        if user_input in VALID_SHOW_PASSWORD_OPTIONS:
            return user_input == 's'
        else:
            print(INVALID_SHOW_PASSWORD_OPTION_MSG)

def parse_args():
    """
    Parse command-line arguments for the password generator.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument('-l', '--length', type=int, help=HELP_MSG_LENGTH)
    parser.add_argument('-t', '--types', type=str, help=HELP_MSG_TYPES)
    parser.add_argument('-s', '--show', type=str, choices=VALID_SHOW_PASSWORD_OPTIONS, help=HELP_MSG_SHOW)
    args = parser.parse_args()

    if args.length and not (MIN_PASSWORD_LENGTH <= args.length <= MAX_PASSWORD_LENGTH):
        parser.error(INVALID_ARG_LENGTH_MSG)

    if args.types:
        selected_char_types = args.types.lower().strip().split(' ')
        if not all(option in CHAR_TYPES_MAP.keys() for option in selected_char_types):
            parser.error(INVALID_ARG_CHAR_TYPES_MSG)

    if args.show and args.show not in VALID_SHOW_PASSWORD_OPTIONS:
        parser.error(INVALID_ARG_SHOW_MSG)

    return args
