# -------------------------------------------------
# x = int(input('nermucel tiv '))
# y = int(input('nermucel tiv '))

# if x > y:
#     for i in range(x, x * y + 1, x):
#         if i % y == 0:
#             print(i)
#             break
# elif y > x:
#     for i in range(y, x * y + 1, y):
#         if i % x == 0:
#             print(i)
#             break
# else:
#     print(x)
# -------------------------------------------------
# n1, n2 = 0, 1
# for i in range(40):
#     print(n1)
#     n1, n2 = n2, n1 + n2
# -------------------------------------------------
# text = input('Enter text: ')
# letter_count = 0
# number_count = 0
# char_count = 0
# for i in text:
#     if i.isdigit():
#         number_count += 1
#     elif i.isalpha():
#         letter_count += 1
#     else:
#         char_count += 1
# print(f'in {text} text -> {number_count} numbers and {letter_count} letters and chars {char_count}')
# -------------------------------------------------
# count = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         count += 1
# print(count)
# -------------------------------------------------
# number = input('Enter Number: ')
# summ = 0
# for i in number:
#     summ += int(i)
# print(summ)
# -------------------------------------------------
# n = int(input('Enter number: '))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)
# -------------------------------------------------
# alphabet = 'XYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# text = input('Enter text: ')
# for i in text:
#     print(alphabet[alphabet.index(i) + 3], end='')
# -------------------------------------------------
# text = input('Enter text: ')
# result = ''
# for i in text:
#     if i == 'X':
#         result += 'A'
#     elif i == 'Y':
#         result += 'B'
#     elif i == 'Z':
#         result += 'C'
#     else:
#         result += chr(ord(i) + 3)
# print(result)
# -------------------------------------------------
# for i in range(0, 101, 10):
#     print(f'{i}(C) = {i * 9/5 + 32}(F)')
# -------------------------------------------------
# for i in ('1', '20', '5', '10'):
#     for j in 'abc':
#         print(f'{i + j:>4}', end=' ')
#     print()
# -------------------------------------------------

# n = int(input('Enter n: '))
# for i in range(n):
#     for j in range(n):
#         if j <= i:
#             print('*', end=' ')
#     print()
# -------------------------------------------------
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>4}', end='')
#     print()
# -------------------------------------------------

# n = int(input('Enter n: '))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# -------------------------------------------------
# pi = 3
# a, b, c = 2, 3, 4
# for i in range(15):
#     pi += 4 / (a * b * c) * ((-1) ** i)
#     a, b, c = a + 2, b + 2, c + 2
# print(pi)
# -------------------------------------------------
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)