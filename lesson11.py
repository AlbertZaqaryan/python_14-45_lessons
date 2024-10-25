# mylist = [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]
# print(mylist[0][1])

# -----------------------------------------------------
# n = int(input('Enter number: '))
# mylist = []
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         mylist.append(i)
# print(mylist)

# n = int(input('Enter number: '))
# print([i for i in range(1, n // 2 + 1) if n % i == 0])

# list1 = []
# list2 = []
# list3 = []
# while True:
#     number = input('Enter number:  ')
#     if number == '':
#         break
#     else:
#         number = int(number)
#         if number < 0:
#             list1.append(number)
#         elif number == 0:
#             list2.append(number)
#         else:
#             list3.append(number)
# print(f'{list1}\n{list2}\n{list3}')


# text = "Contractions!. include: don’t,/ .’..isn’t, and wouldn’t."
# text = text.split(' ')
# mylist = []
# for i in text:
#     while True:
#         if i[0].isalpha() and i[-1].isalpha():
#             mylist.append(i)
#             break
#         elif not i[0].isalpha():
#             i = i[1:]
#         elif not i[-1].isalpha():
#             i = i[:-1]
# print(mylist)
# print(' '.join(mylist))

# -----------------------------------------------------------
# import random

# list1 = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# list2 = ['♥', '♦', '♣', '♠']
# kalod = []
# nor_kalod = []
# for i in list2:
#     for j in list1:
#         kalod.append(i + j)
# while kalod != []:
#     random_cart = random.choice(kalod)
#     nor_kalod.append(random_cart)
#     kalod.remove(random_cart)
# users = [input('Enter user name:   ') for i in range(4)]
# for i in users:
#     print(i, nor_kalod[:8])
#     nor_kalod = nor_kalod[8:]
# -----------------------------------------------------------
# import random
# import os
# import msvcrt


# kapik_i = random.randint(1, 18)
# kapik_j = random.randint(1, 18)

# while True:
#     for i in range(20):
#         for j in range(20):
#             if i == kapik_i and j == kapik_j:
#                 print('🐒', end=' ')
#             else:
#                 print('.', end='  ')
#         print()
#     step = str(msvcrt.getwch()).upper()
#     if step == 'W':
#         kapik_i -= 1
#     elif step == 'S':
#         kapik_i += 1
#     elif step == 'A':
#         kapik_j -= 1
#     elif step == 'D':
#         kapik_j += 1
#     elif step == 'Q':
#         break
#     else:
#         print('ERROR')
#     os.system('cls')
# -----------------------------------------------------------
# mylist = [1, 2, 3, 4]
# newlist = []
# for i in range(1, len(mylist) + 1):
#     for j in range(0, i):
#         newlist.append(mylist[j:i])
# newlist.sort(key=len)
# print(newlist)
# -----------------------------------------------------------
# [8, 65, 78, 90, 11, 60]
# import random

# mylist = []
# while len(mylist) < 6:
#     number = random.randint(1, 100)
#     if number not in mylist:
#         mylist.append(number)
# print(mylist)
# -------------------------------------------------
# import random

# s = ''
# for i in range(8):
#     s += chr(random.randint(33, 127))
# print(s)
# -------------------------------------------------
# text = 'Herb the sage eats sage, the herb'