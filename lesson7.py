# ---------------------------------------------
# for i in range(6):
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>3}', end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter number: '))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter n: '))
# for i in range(0, n + 1):
#     for j in range(0, n + 1):
#         if j == 0 or i == 0 and j == n or j == n:
#             print('|', end=' ')
#         elif i == 0 or i == n:
#             print('-', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# ---------------------------------------------
# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i == j or n == i + j:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# ---------------------------------------------
# name = 'Beno'
# age = 20
# print(f'name = {name}, age = {age}')
# ---------------------------------------------
# import math

# number_count = int(input('Enter number count: '))
# count = 0
# for _ in range(number_count):
#     number = int(input('Enter number: '))
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             break
#     else:
#         count += 1
# print(count)
# ---------------------------------------------
# n = int(input('Enter number: '))
# summ = 0
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     summ += fact
# print(summ)
# ---------------------------------------------
# number_count = int(input('Enter number count: '))
# max_number = 0
# for i in range(number_count):
#     number = int(input('Enter number:  '))
#     temp_sum = 0
#     for i in str(number):
#         temp_sum += int(i)
#     if temp_sum > max_number:
#         max_number = temp_sum
# print(max_number)
# ---------------------------------------------
# for i in range(6):
#     print(i)

# i = 0
# while i < 6:
#     print(i)
#     i += 1

# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break

# ------------------------------------------
# kassa = 0
# while True:
#     age = int(input('Enter age: '))
#     if age == 0:
#         print(kassa)
#         break
#     elif 3 > age > 0:
#         continue
#     elif 12 > age >= 3:
#         kassa += 14
#     elif 65 > age >= 12:
#         kassa += 23
#     else:
#         kassa += 18
# ------------------------------------------
