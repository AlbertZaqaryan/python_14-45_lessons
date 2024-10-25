# ------------------------------------------------------
# n = int(input('Enter number: '))
# start = 0
# stop = 100
# while True:
#     pc_number = (start + stop) // 2
#     print(pc_number)
#     check = int(input('1 or 2 or 3: '))
#     if check == 3:
#         print(pc_number, 'URA')
#         break
#     elif check == 2: # n > pc
#         start = pc_number + 1
#     elif check == 1: # n < pc
#         stop = pc_number - 1
#     print(pc_number, 'CHKPAV')
# ------------------------------------------------------
# 75, 82, 83, 84, 81

# summ = 0
# count = 0
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         if count == 0 and number == '0':
#             continue
#         else:
#             summ += int(number)
# print(summ)
# ------------------------------------------------------
# name = input('Enter name: ')
# print(name == name[::-1])
# ------------------------------------------------------
# text = input('Enter bin text: ')
# text = text[::-1]
# number = 0
# for i in range(0, len(text)):
#     number += int(text[i]) * 2 ** i
# print(number)
# ------------------------------------------------------
# n = int(input('Enter decimal number: '))
# s = ''
# while True:
#     if n == 1:
#         break
#     else:
#         s += str(n % 2)
#         n //= 2
# print('1' + s[::-1])
# ------------------------------------------------------
# import random

# first_number = random.randint(1, 100)
# print(first_number)
# for i in range(99):
#     number = random.randint(1, 100)
#     if number > first_number:
#         print(number, 'update')
#         first_number = number
#     else:
#         print(number)
# ------------------------------------------------------
# import random

# for i in range(10):
#     count_O = 0
#     count_P = 0
#     s = ''
#     while True:
#         if count_O == 3 or count_P == 3:
#             print(s)
#             break
#         else:
#             pc = random.choice("OP")
#             s += pc
#         if pc == 'O':
#             count_O += 1
#             count_P = 0
#         else:
#             count_P += 1
#             count_O = 0
# ------------------------------------------------------
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# for i in range(a):
#     print(b * '=', c * '*',  b * '=')
# ------------------------------------------------------
# 1 - n
# n = 1000
# count = 0
# for i in range(2, n):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         count += 1
# print(count)

# --------------------------
# text = 'python'
# for i in range(1, len(text) + 1):
#     print(text[:i])
# for i in range(len(text) - 1, 0, -1):
#     print(text[:i])
# 'p'
# 'py'
# 'pyt'
# 'pyth'
# 'pytho'
# 'python'
# 'pytho'
# 'pyth'
# 'pyt'
# 'py'
# 'p'


'''
     *
    ***
   *****
  *******
'''