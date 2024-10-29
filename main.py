import random
import pyperclip
import string
from input import prompt_for_password_length

HEADER = "\n# # # # # PASSWORD GENERATOR # # # # #\n"
COMPLEXITY_MSG = "\n# Digite separado por espaços (padrão 'a b n s'): "
SUCESS_MSG = "\n# Senha copiada para o clipboard!\n"

print(HEADER)

password_length = prompt_for_password_length()

uppercase_alphabet = string.ascii_uppercase
lowercase_alphabet = string.ascii_lowercase
numbers = string.digits
symbols = "#$%&()*+-<=>?!@[\]_{|}"

# complexity menu
print("\n# Decida a complexidade...\n")
print("\t> letras maísculas: digite 'a'")
print("\t> letras minúsculas: digite 'b'")
print("\t> dígitos: digite 'n'")
print("\t> símbolos: digite 's'")

complexity_list = (input(COMPLEXITY_MSG) or 'a b n s') \
    .lower().split(' ')

# complexity keys and their charsets
complexity_dict = {
    'a': uppercase_alphabet,
    'b': lowercase_alphabet,
    'n': numbers,
    's': symbols
}

# generating password
all_chars = ''
for i in complexity_list:
    all_chars += ''.join(complexity_dict[i])

password = ''

# ensures there is one character of each type randomly
random_keys = list(complexity_dict.keys())
random.shuffle(random_keys)
for k in random_keys:
    if k in complexity_list:
        password += random.sample(complexity_dict[k], 1)[0]

# generating 
password += ''.join(random.sample(all_chars,
                    password_length - len(complexity_list)))

# copying password to clipboad
pyperclip.copy(password)

print(SUCESS_MSG)