# ------------------------------------------------------------
# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)
# ------------------------------------------------------------
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))
# ------------------------------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
#     #             fib(4) + fib(5)
#     #             fib(2) + fib(3) + fib(5)
#     #             fib(0) + fib(1) + fib(1) + fib(2) + fib(5)
#     #               0 + 1 + 1 + fib(0) + fib(1) + fib(5)
#     #               0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
#     #               0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
#     #               0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
#     #               0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
#     #               0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
#     #               0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)  
#     #               0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1) 
#     #               0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8 
# print(fib(6))
# ------------------------------------------------------------
# def mult(mylist):
#     if mylist == []:
#         return 1
#     else:
#         return mylist[0] * mult(mylist[1:])
                # 8 * mult([4, 5, 6, 9, 10, 6]) 
               # 8 * 4 * mult([5, 6, 9, 10, 6])
               # 8 * 4 * 5 * mult([6, 9, 10, 6])
               # 8 * 4 * 5 * 6 * mult([9, 10, 6])
               # 8 * 4 * 5 * 6 * 9 * mult([10, 6])
               # 8 * 4 * 5 * 6 * 9 * 10 * mult([6])
               # 8 * 4 * 5 * 6 * 9 * 10 * 6 * 1

# print(mult([8, 4, 5, 6, 9, 10, 6]))
# ------------------------------------------------------------
# def alo(a, b):
#     if b == 0:
#         return a
#     else:
#         return alo(b, a % b)
# print(alo(12, 15))

# ------------------------------------------------------------

# def func(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + func(mylist[2:])

# print(func(["A", 12, "B", 4, "A", 6, "B", 1]))
# # ["A", "A", "A", "A", "A", "A", "A", "A", "A","A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"] 
# ------------------------------------------------------------


# def func(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == list:
#         return func(mylist[0]) + func(mylist[1:])
#     else:
#         return [mylist[0]] + func(mylist[1:])

# print(func([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]))
# ------------------------------------------------------------

# def find_prefix(strs, index=1): 
#     if index == len(strs):
#         return strs[0]
#     elif strs[0] == strs[index][:len(strs[0])]:
#         return find_prefix(strs, index + 1)
#     else:
#         strs[0] = strs[0][:-1]
#         return find_prefix(strs, index)
 
# print(find_prefix(["flower","flow","flight"]))
# ------------------------------------------------------------
