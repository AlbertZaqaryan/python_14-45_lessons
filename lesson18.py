# def is_prime(number):
#     for i in range(2,int(number ** 0.5) + 1):
#         if number % i == 0:
#             return 'Parz che'
#     else:
#         return 'Parz e'

# number = int(input('Enter number: '))
# print(is_prime(number))
# print(is_prime(34))

# --------- 85 ------------  ### AMOT
# def Pifagor(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c

# print(Pifagor(3, 4))

# --------- 86 ------------  ### AMOT x2
# def taxi(km):
#     return f'${round(4 + (km * 1000 / 140) * 0.25)}'

# print(taxi(2.5))

# --------- 87 ------------  ### AMOT x3
# def delivery(count):
#     return 10.95 + (count - 1) * 2.95
# print(delivery(3))
# --------- 88 ------------  ### AMOT x4
# def median(a, b, c):
#     mylist = [a, b, c]
#     mylist.sort()
#     return mylist[1]
# print(median(-6, 9, 3))
# --------- 89 ------------  ### AMOT x10
# def number_to_text(number):
#     text_ = {
#         1:'One',
#         2:'Two',
#         3:'Three',
#         4:'Four',
#         5:'Five',
#         6:'Six',
#         7:'Seven',
#         8:'Eight',
#         9:'Nine',
#         10:'Ten',
#         11:'Eleven',
#         12:'Twelve'
#     }
#     return text_[number]
# print(number_to_text(11))
# --------- 91 ------------

# def calendar(day, month, year):
#     summ = 0
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     for i in range(month - 1):
#         summ += day_list[i]
#     summ += day
#     return summ
# print(calendar(31, 12, 2023))

# --------- 92 ------------

# def reverse_calendar(year, days):
#     month = 1
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     while True:
#         if days > day_list[0]:
#             days -= day_list[0]
#             month += 1
#             day_list.pop(0)
#         else:
#             break
#     return f'{days}.{month}.{year}'

# print(reverse_calendar(2024, 297))

# 00 XX 000
# ------------------------------------------------------
# import random

# def random_numbers():
#     alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     return f'{random.randint(0, 9)}{random.randint(0, 9)} {random.choice(alphabet)}{random.choice(alphabet)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
# print(random_numbers())
# ------------------------------------------------------
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>4}', end=' ')
#     print()
# ------------------------------------------------------

# def factorial(number):
#     summ = 1
#     for i in range(1, number + 1):
#         summ *= i
#     return summ
# print(factorial(5))


# (18) - ('10010')

# def dec_to_bin(number):
#     binary_code = ''
#     while number > 1:
#         binary_code += str(number % 2)
#         number //= 2
#     return '1' + binary_code[::-1]
# print(dec_to_bin(120))

# def bin_to_dec(bin_code):
#     bin_code = bin_code[::-1]
#     number = 0
#     for i in range(0, len(bin_code)):
#         number += int(bin_code[i]) * (2 ** i)
#     return number
# print(bin_to_dec('1100'))

