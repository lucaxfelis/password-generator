from constants import (
    COMPLEXITY_MAP,
    COMPLEXITY_MSG,
    DEFAULT_PASSWORD_LENGTH,
    INVALID_DIGIT_MSG,
    INVALID_LENGTH_MSG,
    LENGTH_MSG,
    MIN_PASSWORD_LENGTH,
    MAX_PASSWORD_LENGTH
)

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

def prompt_for_password_complexity() -> list:
    """
    Prompt the user to enter the desired password complexity.
    
    Returns:
        list: A list of selected complexities in lowercase.
    """
    while True:
        complexity_list = (input(COMPLEXITY_MSG) or 'a b n s').lower().strip().split(' ')
        if all(option in COMPLEXITY_MAP.keys() for option in complexity_list):
            return complexity_list
        else:
            print("Invalid complexity options. Please enter valid options: 'a', 'b', 'n', 's'.")