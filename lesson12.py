# -------------------------------------------------------------
# import random
# import os
# import msvcrt


# kapik_i = random.randint(1, 18)
# kapik_j = random.randint(1, 18)

# banan_i = random.randint(1, 18)
# banan_j = random.randint(1, 18)

# kapik_miavorner = 0

# while True:
#     print('Kapiki miavorner', kapik_miavorner)
#     for i in range(20):
#         for j in range(20):
#             if i == kapik_i and j == kapik_j:
#                 print('🐒', end=' ')
#             elif i == banan_i and j == banan_j:
#                 print('🍌', end=' ')
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
#     if kapik_i == banan_i and kapik_j == banan_j:
#         kapik_miavorner += 1
#         banan_i = random.randint(1, 18)
#         banan_j = random.randint(1, 18)
#     os.system('cls')
# -------------------------------------------------------------
# ------------------------ dictionary -------------------------
# x = {"a":1, "b":2}

# {key:value}

# x = {
#     'a':[1, 2, 3],
#     "b":2,
#     "c":2,
#     "d":2,

# }
# print(x)

# list1 = [1, 2, 3]
# list2 = list1
# list2.append(4)
# print(list1)


# mycars = [
#     {
#         "model":"Fiat",
#         "motor":1.2,
#         "price":8000
#     },
#     {
#         "model":"BMW",
#         "motor":4.8,
#         "price":30000
#     },
#     {
#         "model":"Opel astra S",
#         "motor":1.6,
#         "price":1
#     }
# ]
# print(mycars)


# data = {
#     "a":1,
#     "b":2,
#     "c":-10,
#     "d":5
# }
# print(data["a"])
# --- get ---
# print(data['Ճ'])
# print(data.get('a', 'Chka'))
# keys = sorted(data, key=data.get)
# print(keys)

# data["a"] = 34
# data['Ճ'] = "Սերգո"
# print(data)

# data.popitem()
# print(data)

# data.pop("b")
# print(data)


# data = {
#     "a":1,
#     "b":2,
#     "c":-10,
#     "d":5
# }
# data.clear()
# print(data)

# for i in data:
#     print(data[i])

# print(data.keys())
# print(data.values())
# print(data.items())

# x = ([('a', 1), ('b', 2), ('c', -10), ('d', 5)])
# print(dict(x))


# data1 = {
#     "a":1,
#     "b":2,
#     "c":-10,
#     "d":5
# }

# data2 = {
#     "e":1,
#     "g":2,
#     "g":-10,
#     "l":5
# }

# data1.update(data2)
# print(data1)
# -----------------------------------------------

# data = {
#     'a':10, 'b':30
# }
# summ = 0
# for i in data:
#     summ += data[i]
# print(summ)


# d = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys = sorted(d, key=d.get, reverse=True)[:3]
# test = {}
# for i in keys: # ['F', 'A', 'D']
#     test[i] = d[i]
# print(test)


# d = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:d[i] for i in sorted(d, key=d.get, reverse=True)[:3]})


# dict_ = {
#     'a':1,
#     'b':2,
#     'c':2,
#     'd':1,
#     'e':3
# }

# new_dict = {}
# for i in dict_: # i = 'a', dict_[i] = 1
#     if dict_[i] in new_dict:
#         new_dict[dict_[i]].append(i)
#     else:
#         new_dict[dict_[i]] = [i]
# print(new_dict)

# s = 'a,2,c,4,a,4,e,11,d,20'
# s = s.split(',')
# data = {}
# for i in range(0, len(s) - 1, 2):
#     if s[i] in data:
#         data[s[i]] += int(s[i + 1])
#     else:
#         data[s[i]] = int(s[i + 1])
# print(data)
# {'a':6, 'c':4, 'e':11, 'd':20}


# students = {
#     'Sergo':-1,
#     'Gev':2,
#     'Maria':10,
# }


