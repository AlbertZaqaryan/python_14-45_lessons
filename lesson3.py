# 9, 13, 30, 31, 32, 33, 34 գրքից տնային
# ------------- book n9 -------------------
# sum_ = int(input('Enter sum: '))
# year_1 = sum_ + sum_ * 4 / 100
# year_2 = year_1 + year_1 * 4 / 100
# year_3 = year_2 + year_2 * 4 / 100
# print(f'Start sum = {sum_}\nyear 1 = {year_1}\
#       \nyear 2 = {year_2}\nyear 3 = {year_3}')
# ------------- book n13 -------------------
# number = int(input('Ener your number: '))
# count_200 = number // 200
# number %= 200
# count_100 = number // 100
# number %= 100
# count_25 = number // 25
# number %= 25
# count_10 = number // 10
# number %= 10
# count_5 = number // 5
# number %= 5
# count_1 = number // 1
# print(f'200({count_200})\n100({count_100})\n25({count_25})\n10({count_10})\n5({count_5})\n1({count_1})')
# ------------- book n30 -------------------
# celsus = float(input('Enter celsus value: '))
# far = celsus * 9/5 + 32
# print(f'{celsus}(celsus) = {far}(far)')
# ------------- book n31 -------------------
# number = int(input('Enter 4 numbers: '))
# x4 = number % 10
# number //= 10
# x3 = number % 10
# number //= 10
# x2 = number % 10
# number //= 10
# x1 = number % 10
# print(x1 + x2 + x3 + x4)
# ------------- book n33 -------------------
# number1 = int(input('Enter number1: '))
# number2 = int(input('Enter number2: '))
# number3 = int(input('Enter number3: '))
# min_number = min(number1, number2, number3)
# sum_number = sum((number1, number2, number3))
# max_number = max(number1, number2, number3)
# print(min_number, sum_number - min_number - max_number, max_number)
# ------------- book n34 -------------------
# count = int(input('Enter count:  '))
# price = 3.49
# print(count * price, count * (price - price * 60 / 100))
# ---------------------------------------------------------
# angle1 = int(input('Enter angle1: '))
# angle2 = int(input('Enter angle2: '))
# print(angle1 + angle2 == 90)
# ---------------------------------------------------------
# ---------------------- logic operators ------------------------
# ---------------------------------------------------------
# print(5 & 6)
# print(5 | 6)
# print(5 ^ 6)

# ---------------------------------------------------------

# print(5 > 4 and 6 > 3)
#    True  and  True = True
#      1 & 1 = 1
# ---------------------------------------------------------

# print(10 < 2 and 4 > 1)
#     False  and  True = False
#       0  &   1  = 0
# ---------------------------------------------------------

# print(10 >= 10 and 10 == 3 or 5 > 3 and 4 < -6)
#       True and   False  or True  and False
#             False   or   True and False
#                  True  and False
#                       False
# ---------------------------------------------------------


# print(not False)
# ---------------------------------------------------------


# text = 'Python'
# print('tPy' not in text)
# ---------------------------------------------------------


# x = 5
# y = 5
# print(x is y)
# print(x == y)
# ---------------------------------------------------------

# x = '5'
# y = 'a'
# print(y.isalpha())
# print(x.isdigit())
# ---------------------------------------------------------

# text = input('Enter text:  ')
# print(text.isupper())
# print(not text.islower())
# ---------------------------------------------------------
# x = 6
# print(5 < 3 or x == y)
#    False  or   NameError
# ---------------------------------------------------------
# a = 5
# b = 7
# # a = a + b # 12
# # b = a - b # 5
# # a = a - b # 7
# a, b = b, a # swap
# print(a, b)
# ---------------------------------------------------------
