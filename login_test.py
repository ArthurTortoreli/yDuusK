# coding=utf-8

from passlib.hash import pbkdf2_sha256 as cryp


class User:

    users = 0

    def __init__(self, name, surname, email0, password0):
        self.__id = User.users + 1
        self.__name = name
        self.__surname = surname
        self.__email = email0
        self.__password = cryp.hash(password0, rounds=200000, salt_size=16)
        User.users = self.__id

    def check_password(self, password1):
        """Checks the validity of the password entered"""
        if cryp.verify(password1, self.__password):
            return True
        return False

    def check_user(self, email1):
        """Checks the validity of the informed user"""
        if email1 != self.__email:
            return False
        return True


name_typed = input('Enter your name: ')
surname_typed = input('Enter your last name: ')
email_typed = input('Enter your email: ')
password_typed = input('Enter a password: ')
confirm_password = input('Confirm the Password: ')

if password_typed == confirm_password:
    user = User(name_typed, surname_typed, email_typed, password_typed)
else:
    print('Passwords do not match!')
    exit(42)

print('User created successfully!\n')

cont = 0

while cont != 1:
    email = input('User: ')
    password = input('Password: ')

    if user.check_user(email):
        if user.check_password(password):
            print(f'Welcome! {name_typed}!')
            print(f'Encrypted User Password: {user._User__password}')  # Just for study
            cont += 1
        else:
            print('Incorrect username or password.')
            cont = 0
    else:
        print('Incorrect username or password.')
        cont = 0

