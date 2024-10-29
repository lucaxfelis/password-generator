import string


DEFAULT_PASSWORD_LENGTH = 16
MAX_PASSWORD_LENGTH = 32
MIN_PASSWORD_LENGTH = 6

LENGTH_MSG = f"# Digite o tamanho da senha (padrão: {DEFAULT_PASSWORD_LENGTH}, min: {MIN_PASSWORD_LENGTH}, max: {MAX_PASSWORD_LENGTH}): "
INVALID_LENGTH_MSG = f"\n⚠️  Por favor, digite um tamanho entre {MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}.\n"
INVALID_DIGIT_MSG = "\n⚠️  Entrada inválida. Por favor, digite um número válido.\n"

UPPERCASE_ALPHABET = string.ascii_uppercase
LOWERCASE_ALPHABET = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = "#$%&()*+-<=>?!@[\]_{|}"

UPPERCASE_ALPHABET_KEY = 'a'
LOWERCASE_ALPHABET_KEY = 'b'
NUMBERS_KEY = 'n'
SYMBOLS_KEY = 's'

CHAR_TYPES_MAP = {
    UPPERCASE_ALPHABET_KEY: UPPERCASE_ALPHABET,
    NUMBERS_KEY: LOWERCASE_ALPHABET,
    NUMBERS_KEY: NUMBERS,
    SYMBOLS_KEY: SYMBOLS
}

CHAR_TYPES_MENU_MSG = f"""
    # Decida os tipos de caracteres incluídos na senha...

        > letras maísculas: digite '{UPPERCASE_ALPHABET_KEY}'
        > letras minúsculas: digite '{LOWERCASE_ALPHABET_KEY}'
        > dígitos: digite '{NUMBERS_KEY}'
        > símbolos: digite '{SYMBOLS_KEY}'
    """
CHAR_TYPES_MSG = f"\n# Digite-os separados por espaços (padrão '{' '.join(CHAR_TYPES_MAP.keys())}'): "
VALID_CHAR_TYPES_OPTIONS = ', '.join(map(lambda type: f"'{type}'", CHAR_TYPES_MAP.keys()))
INVALID_CHAR_TYPES_MSG = f"Invalid char types options. Please enter valid options: {VALID_CHAR_TYPES_OPTIONS}"




