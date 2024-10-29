import string


DEFAULT_PASSWORD_LENGTH = 16
MAX_PASSWORD_LENGTH = 32
MIN_PASSWORD_LENGTH = 6

HEADER = "\n# # # # # PASSWORD GENERATOR # # # # #\n"

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
    LOWERCASE_ALPHABET_KEY: LOWERCASE_ALPHABET,
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
INVALID_CHAR_TYPES_MSG = f"\n⚠️  Opções para tipos de caracteres inválidas. Por favor, digite opções válidas: {VALID_CHAR_TYPES_OPTIONS}"

SHOW_PASSWORD_OPTIONS_MSG = "\n# Mostrar a senha gerada? (s/N): "
VALID_SHOW_PASSWORD_OPTIONS = {'s', 'n'}
INVALID_SHOW_PASSWORD_OPTION_MSG = "\n⚠️  Opção inválida. Digite 's' para mostrar a senha ou 'n' para escondê-la."
GENERATED_PASSWORD = "\n# Senha gerada: {}"

HELP_MSG_LENGTH = f"Tamanho da senha (padrão: {DEFAULT_PASSWORD_LENGTH}, min: {MIN_PASSWORD_LENGTH}, max: {MAX_PASSWORD_LENGTH})"
HELP_MSG_TYPES = f"Tipos de caracteres (opções válidas: {', '.join(CHAR_TYPES_MAP.keys())})"
HELP_MSG_SHOW = "Mostrar a senha gerada? (s/N)"

INVALID_ARG_LENGTH_MSG = f"\n⚠️  Tamanho inválido. Por favor, digite um tamanho entre {MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}."
INVALID_ARG_CHAR_TYPES_MSG = f"\n⚠️  Tipos de caracteres inválidos. Por favor, digite opções válidas: {VALID_CHAR_TYPES_OPTIONS}."
INVALID_ARG_SHOW_MSG = "\n⚠️  Opção inválida para mostrar a senha. Digite 's' para mostrar a senha ou 'n' para escondê-la."

SUCESS_MSG = "\n# Senha gerada com sucesso e copiada para o clipboard! 🔐\n"
