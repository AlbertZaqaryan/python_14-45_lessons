# x = [3, 1, 2, 1, 1, 4]
# count = 0
# while count < len(x):
#     qayler = x[count]
#     print(f'nerkayis tiv: {count}, catker: {qayler}')
#     count += qayler
#     if count >= len(x):
#         print('duq partveciq')
#         break
#     elif count == len(x) - 1:
#         print('duq haxtel eq')
#         break
#     elif qayler == 0:
#         print('duq partveciq')
#         break
# ---------------------------------------------------

# x = [3, 1, 2, 1, 0, 4]
# index = 0
# while True:
#     step = x[index]
#     index += step
#     if index == len(x) - 1:
#         print('You win')
#         break
#     elif step == 0:
#         break
#     elif index >= len(x):
#         break
# ---------------------------------------------------
# ------------------------- set ---------------------
# set1 = set()
# set2 = {}
# {'a':1}
# {'a', 1}


# set1 = {1, 2, 3, 4, 1, 2, 3}
# set2 = {0, -6, 33}
# print(set1.isdisjoint(set2))


# set1 = {5, 4, 16, 3, 6, 0}
# print(set1[5])
# print(hash('a'))



# set1 = {1, 2, 3}
# set1.add(4)
# set1.discard(3)
# print(set1)

# set1 = {1, 2, 3}
# set2= {3, 4}
# set3 = set1.union(set2)
# print(set3)

# set1 = {1, 2, 3}
# set2 = {1, 2}
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set1.difference(set2))

# list1 = [1, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7]
# print(list(set(list1)))

# mylist = [7, 9, 10, 15, 30, 45, 90, 130, 150, 265, 300, 450, 690, 1720, 3020]
# n = 1720
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if n == mylist[mid]:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1


# Big(O)


# mylist = [7, 9, 10, 15, 30, 45, 90, 130, 150, 265, 300, 450, 690, 1720, 3020]
# n = 1720
# for i in range(0, len(mylist)):
#     pass # O(n)

# n = 1720 # O(logn)
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if n == mylist[mid]:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1


# mylist = [7, 5, 4, 1, 2, 6, 9]
# for i in range(0, len(mylist)): # o(n)
#     for j in range(0, len(mylist)): # o(n)


# mylist = [7, 5, 4, 1, 2, 6, 9]
# for i in range(0, len(mylist)): # o(n)
#     if i % 2 == 0:
#         mylist.insert(1, '$') # o(n)
# print(mylist)


# print([i for i in range(10)])
# x = (i for i in range(10))
# print(next(x))
# print(next(x))
# print(next(x))


# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c']
# for i, j in zip(list1, list2):
#     print(i, j)

# for i in range(min(len(list1), len(list2))):
#     print(list1[i], list2[i])



