from input import parse_args, prompt_for_password_char_types, prompt_for_password_length, prompt_for_show_password
from output import print_char_types_menu, print_header, print_sucess_msg, show_password
from password_generator import copy_password_to_clipboard, generate_password, get_available_characters


def main():
    print_header()

    args = parse_args()

    if args.length:
        password_length = args.length
    else:
        password_length = prompt_for_password_length()

    print_char_types_menu()
    if args.types:
        selected_char_types = args.types.lower().strip().split(' ')
    else:
        selected_char_types = prompt_for_password_char_types()

    available_chars = get_available_characters(selected_char_types)
    password = generate_password(available_chars, selected_char_types, password_length)

    if args.show and args.show == 's':
        show_password(password)
    elif not args.show:
        if prompt_for_show_password():
            show_password(password)

    copy_password_to_clipboard(password)
    print_sucess_msg()

if __name__ == "__main__":
    main()