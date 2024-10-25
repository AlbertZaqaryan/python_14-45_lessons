# mylist = [7, 4, -6, 0, 8, 9, 1]
# number = 11
# mylist.sort() # n^log(n)
# for i in mylist:
#     start = 0
#     stop = len(mylist)
#     while True:
#         mid = (start + stop) // 2
#         if mylist[mid] == number - i:
#             print(True)
#             break
#         elif mylist[mid] > number - i:
#             stop = mid - 1
#         else:
#             start = mid + 1
# else:
#     print(False)

# mylist = [2]
# for number in range(3, int(input('Enter n: ')) + 1, 2):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             break
#     else:
#         mylist.append(number)
# print(mylist)


# mylist = [180, -1, 150, 160, -1, -1, 190, 170]
# newlist = [i for i in mylist if i != -1]
# newlist.sort()
# i, j = 0, 0
# while i < len(mylist):
#     if mylist[i] == -1:
#         i += 1
#     else:
#         mylist[i] = newlist[j]
#         i += 1
#         j += 1
# print(mylist)

# mylist = [5, -3, 6, 7, 1, 2, 4]
# print(max([mylist[i] * mylist[i + 1] for i in range(0, len(mylist) - 1)]))
# newlist = []
# for i in range(0, len(mylist) - 1):
#     newlist.append(mylist[i] * mylist[i + 1])
# print(max(newlist))

