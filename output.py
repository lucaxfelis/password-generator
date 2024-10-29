from constants import CHAR_TYPES_MENU_MSG, GENERATED_PASSWORD, HEADER, SUCESS_MSG


def print_char_types_menu() -> None:
    """
    Print the char types menu for password generation options.
    """
    print(CHAR_TYPES_MENU_MSG)


def print_header() -> None:
    """
    Print the header for the password generator.
    """
    print(HEADER)


def print_sucess_msg() -> None:
    """
    Print the success message after generating a password.
    """
    print(SUCESS_MSG)


def show_password(password: str) -> None:
    """
    Print the generated password.
    
    Args:
        password (str): The generated password.
        show (bool): Whether to show the password.
    """
    print(GENERATED_PASSWORD.format(password))
