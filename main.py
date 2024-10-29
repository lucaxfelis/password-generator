import random
import pyperclip
from constants import COMPLEXITY_MAP
from input import prompt_for_password_complexity, prompt_for_password_length
from output import print_complexity_menu

HEADER = "\n# # # # # PASSWORD GENERATOR # # # # #\n"
SUCESS_MSG = "\n# Senha copiada para o clipboard!\n"



print(HEADER)

password_length = prompt_for_password_length()

print_complexity_menu()
complexity_list = prompt_for_password_complexity()

complexity_dict = COMPLEXITY_MAP

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