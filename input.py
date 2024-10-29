from constants import (
    DEFAULT_PASSWORD_LENGTH,
    INVALID_DIGIT_MSG,
    INVALID_LENGTH_MSG,
    LENGTH_MSG,
    MIN_PASSWORD_LENGTH,
    MAX_PASSWORD_LENGTH,
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