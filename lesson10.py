# --------------------------------------------
# n = 10
# for i in range(n):
#     for j in range(2 * n):
#         if j <= i:
#             print(n - j, end='')
#         elif j >= 2 * n - 1 - i:
#             print(j - n + 1, end='')
#         else:
#             print('-',end='')
#     print()
# --------------------------------------------
# text = 'Sergo'
# print([text])
# --------------------------------------------
# mylist = ['S', 'e', 'r', 'g', 'o', ' ', 'l', 'i', 'k', 'e', ' ', 'f', 'u', 't', 'b', 'o', 'l']
# text = ''.join(mylist)
# print(text)

# text = 'Sergo like coffee'
# text = text.split(' ')
# print(text)

# mylist = [7, 8, 50, 1, 2, 3, 6, 9, 8]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

# mylist = [7, 8, 50, 1, 2, 3, 6, 9, 8]
# print([i for i in mylist if i % 2 == 0])

# mylist = [7, 8, 50, 1, 2, 3, 6, 9, 8]
# print(['Even' if i % 2 == 0 else 'Odd' for i in mylist])

# ------------------------------------------------------
# import random


# users1 = ['Sergo', 'Vazgen', 'Anushik', 'Maria', 'Erik']
# users2 = ['Sergo', 'Vazgen', 'Anushik', 'Maria', 'Erik']
# final_list = []
# while True:
#     if users1 == [] == users2:
#         break
#     u1 = random.choice(users1)
#     u2 = random.choice(users2)
#     if u1 != u2:
#         final_list.append(f'{u1} ---- {u2}')
#         users1.remove(u1)
#         users2.remove(u2)
#     else:
#         continue
#     if users1 == users2 and len(users1) == 1 == len(users2):
#         users1 = ['Sergo', 'Vazgen', 'Anushik', 'Maria', 'Erik']
#         users2 = ['Sergo', 'Vazgen', 'Anushik', 'Maria', 'Erik']
#         final_list = []
#         continue
# for i in final_list:
#     print(i)
# ------------------------------------------------------
# n = int(input('Enter n: '))
# numbers = []
# for i in range(2, n + 1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         numbers.append(i)
# print(numbers)
# ------------------------------------------------------
# n = 10000
# 28
# 1 + 2 + 4 + 7 + 14 = 28

# 6
# 1 + 2 + 3 = 6

# for number in range(1, 10000):
#     summ = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             summ += i
#     if summ == number:
#         print(number)
# ------------------------------------------------------
