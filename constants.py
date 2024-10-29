import string


DEFAULT_PASSWORD_LENGTH = 16
MAX_PASSWORD_LENGTH = 32
MIN_PASSWORD_LENGTH = 6

LENGTH_MSG = f"# Digite o tamanho da senha (padrão: {DEFAULT_PASSWORD_LENGTH}, min: {MIN_PASSWORD_LENGTH}, max: {MAX_PASSWORD_LENGTH}): "
INVALID_LENGTH_MSG = f"\n⚠️  Por favor, digite um tamanho entre {MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}.\n"
INVALID_DIGIT_MSG = "\n⚠️  Entrada inválida. Por favor, digite um número válido.\n"
COMPLEXITY_MENU_MSG = """
    # Decida a complexidade...

        > letras maísculas: digite 'a'
        > letras minúsculas: digite 'b'
        > dígitos: digite 'n'
        > símbolos: digite 's'
    """
COMPLEXITY_MSG = "\n# Digite separado por espaços (padrão 'a b n s'): "

UPPERCASE_ALPHABET = string.ascii_uppercase
LOWERCASE_ALPHABET = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = "#$%&()*+-<=>?!@[\]_{|}"
COMPLEXITY_MAP = {
    'a': UPPERCASE_ALPHABET,
    'b': LOWERCASE_ALPHABET,
    'n': NUMBERS,
    's': SYMBOLS
}