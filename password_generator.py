import random


def generate_password(length_pass, chars):
    your_password = ''
    for _ in range(length_pass):
        your_password += random.choice(chars)
    return your_password


def is_valid(user_number):
    while not user_number.isdigit():
        print('Введите число!')
        user_number = input()
    return int(user_number)


def is_valid_letters(chars):
    if chars == 'д':
        return True
    elif chars == 'н':
        return False
    else:
        while chars != 'д' and chars != 'н':
            print('Введите "д" или "н"!')
            chars = input()


digits = '123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

quantity = input('Введите количество паролей для генерации: ')
quantity = is_valid(quantity)
length = input('Введите длину пароля: ')
length = is_valid(length)
numbs = input('Включать ли цифры 0123456789? д - да, н - нет:   ')
numbs = is_valid_letters(numbs)
capital_letter = input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д - да, н - нет:   ')
capital_letter = is_valid_letters(capital_letter)
small_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д - да, н - нет:   ')
small_letter = is_valid_letters(small_letter)
symbol = input('Включать ли символы !#$%&*+-=?@^_? д - да, н - нет:   ')
symbol = is_valid_letters(symbol)
exception_symbols = input('Исключать ли неоднозначные символы il1Lo0O? д - да, н - нет:   ')
exception_symbols = is_valid_letters(exception_symbols)


if numbs:
    chars += digits
if capital_letter:
    chars += uppercase_letters
if small_letter:
    chars += lowercase_letters
if symbol:
    chars += punctuation
if exception_symbols:
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')

for _ in range(quantity):
    password = generate_password(length, chars)
    print()
    print(password)
