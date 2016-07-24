import re

def check_password(password):
    lower = re.search("[a-z]", password)
    upper = re.search("[A-Z]", password)
    digit = re.search("[0-9]", password)
    char = re.search("[$@#]", password)
    length = len(password)>=6 and len(password)<=12

    if lower and upper and digit and char and length:
        print('Strong password.')
    else:
        print('Weak password.')

password = input('Please enter your password.\n')

while (password != ''):
    check_password(password)
    password = input('Please enter your password.\n')
