import random
import pyperclip
#import email_sender

print("\n# # # # # PASSWORD GENERATOR # # # # #\n")

password_length = int(input("# Digite a quantidade de caracteres (padrão 16): ") or 16)

# available caracteres
upper_case = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lower_case = [chr(i) for i in range(ord('a'), ord('z') + 1)]
numbers = list('0123456789')
symbols = list('!@#$%&*-+=')

# complexity menu
print("\n# Decida a complexidade...\n")
print("\t> letras maísculas: digite 'a'")
print("\t> letras minúsculas: digite 'b'")
print("\t> dígitos: digite 'n'")
print("\t> símbolos: digite 's'")

complexity_list = \
    (input("\n# Digite separado por espaços (padrão 'a b n s'): ") or 'a b n s') \
    .lower().split(' ')

# complexity keys and their charsets
complexity_dict = {'a': upper_case,
                   'b': lower_case,
                   'n': numbers,
                   's': symbols}

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

print("\n# Senha copiada para o clipboard!\n")