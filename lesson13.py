# new_dict = {
#     "Harut": 1,
#     "Ero":8,
#     "Hrach":4,
#     "Trdat":2,
#     "Tigran":7,
#     "Sona": 12,
#     "Martin": 3,
#     "Sergo": -300,
#     "Albert": 999
# }
# mean_score = sum(new_dict.values()) / len(new_dict)
# list1 = []
# list2 = []
# for i in new_dict:
#     if new_dict[i] >= mean_score:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(f'Good students -> {list1}\nBad students -> {list2}')

# print(new_dict.get(input('Enter name: '), 'No'))

# text = input('Enter text:  ')
# print({i:text.count(i) for i in text})



# mydict = {
#     '1':'.,?!',
#     '2':'ABC',
#     '3':'DEF',
#     '4':'GHI',
#     '5':'JKL',
#     '6':'MNO',
#     '7':'PQRS',
#     '8':'TUV',
#     '9':'WXYZ',
#     '0':' '
# }
# text = input('Enter text:  ') # HELLO   i = 'H'
# for i in text:
#     for j in mydict: # j = '4'   mydict[j] = 'GHI'
#         if i in mydict[j]:
#             print((mydict[j].index(i) + 1) * j, end='')


# text1 = input('Enter text1: ')
# text2 = input('Enter text2: ')
# print({i:text1.count(i) for i in text1} == {i:text2.count(i) for i in text2})
# dict1 = {i:text1.count(i) for i in text1}
# dict2 = {i:text2.count(i) for i in text2}
# print(dict1, dict2)


# dict1 = {}
# text = input('Enter text: ')
# summ = 0
# for i in text:
#     for j in dict1:
#         if i in dict1[j]:
#             summ += j
# print(summ)


# import random

# toms = {
#     'B':[random.randint(1, 15) for i in range(5)], # 1-15
#     'I':[random.randint(16, 30) for i in range(5)], # 16-30
#     'N':[random.randint(31, 45) for i in range(5)], # 31-45
#     'G':[random.randint(46, 60) for i in range(5)], # 46-60
#     'O':[random.randint(61, 75) for i in range(5)], # 61-75
# }
# payman = True
# while payman:
#     input('Enter for continue: ')
#     number = random.randint(1, 75)
#     for i in toms:
#         if toms[i].count('X') == 5:
#             payman = False
#             break
#         if number in toms[i]:
#             toms[i][toms[i].index(number)] = 'X'
#         print(f'{i} : {toms[i]}')
#     print(number)