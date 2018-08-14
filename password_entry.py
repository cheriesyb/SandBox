"""Cherie"""

MIN_LENGTH = 4


def main():
    get_password = validate_password(MIN_LENGTH)
    print('*' * len(get_password))


def validate_password(min_length):
    password = input("Please enter password: ")
    if len(password) < MIN_LENGTH:
        print("Password is too short.")
        password = input("Please enter password: ")
        return password

main()