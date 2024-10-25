# ----------------------------------------------------------
# mylist = ['flower', 'flow', 'flight']
# mylist.sort(key=len)
# # ['flow', 'flower', 'flight']
# index = 1 # 2
# while index < len(mylist):
#     if mylist[0] == mylist[index][:len(mylist[0])]:
#         index += 1
#     else:
#         mylist[0] = mylist[0][:-1]
# print(mylist[0])
# ----------------------------------------------------------
# roman={
#      1:'I',
#      5:'V',
#      10:'X',
#      50:'L',
#      100:'C',
#      500:'D',
#      1000:'M'
# }
# text = 'IIV'
# 1000 + 100 + 4 = 1104 
# ----------------------------------------------------------
# def myfunc():

#     print(10)

# myfunc()
# myfunc()
# myfunc()
# myfunc()
# myfunc()
# myfunc()


# def game():
#     for i in range(20):
#         for j in range(20):
#             print('.', end=' ')
#         print()


# game()



# for i in range(3):
#     game()


# def armat(tiv):
#     print(tiv ** 0.5)


# number = int(input('Enter number: '))
# armat(number)

# return 

# def myfunc():
#     print(5)


# print(myfunc() + 10)


# def myfunc():
#     return 5

# print(myfunc() + 10)

# def game():
#     for i in range(20):
#         for j in range(20):
#             return '.'
#         # print()

# print(game())


# def func():
#     return 10

# print(func())


# def func(number):
#     return str(number) == str(number)[::-1]



# def generate_polidrom_numbers(interval):
#     for i in range(10, interval):
#         if func(i) == True:
#             print(i)

# generate_polidrom_numbers(1000)

# def add(number1, number2, number3=3):
#     return number1 + number2 + number3

# print(add(number1=10, number2=3, number3=4))

# def func(*args):
#     return args

# print(func(10, 5, -6, 3, 5, 9))

# def func(**kwargs):
#     return kwargs

# print(func(x=5, y=7))


# def even_numbers(mylist):

#     newlist = []
#     for i in mylist:
#         if i % 2 == 0:
#             newlist.append(i)
#     return newlist

# print(even_numbers([2, 3, 4, 5, 1, 1]))
# print(even_numbers([9, 8, 5, 10, 4]))
# print(even_numbers([8, 5, 4, 1, 2, 3, 6, 9]))


# def func(number:int|float) -> int|float:
#     '''
#         Ֆունկցիային տվեք թիվ, ֆունկցիան 
#         կվերադարձնի այդ թվի 5 աստիճանը    
        
#     '''
#     return [number ** 5, 10]


# print(func(4))

# def func(number):
#     return 5

# func(8)

# print(number)

# def func():
#     global number
#     number = 4
#     return number

# func()
# print(number)


# def summ(a, b):
#     return a + b
# print(summ(5, 7))

# summ = lambda a, b: a + b
# print(summ(7, 5))



# def summ(n1, n2):
#     return n1 + n2

# def div(n1, n2):
#     return n1 / n2

# def mult(n1, n2):
#     return n1 + n2

# def dif(n1, n2):
#     return n1 - n2

# print(summ(7, 6))
# print(div(10, 2))
# print(mult(8, 3))
# print(dif(10, 3))

# def find_numbers(text):
#     number_count = 0
#     letter_count = 0
#     for i in text:
#         if i.isdigit():
#             number_count += 1
#         elif i.isalpha():
#             letter_count += 1
#     return f'Number count = {number_count}\nLetter count = {letter_count}'

# print(find_numbers('sfashaksa s4a5 46s as ajkl'))

# def is_prime(number):

#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     else:
#         return True
    
# def next_prime(number):
#     number += 1
#     while True:
#         if is_prime(number) == True:
#             return number
#         else:
#             number += 1

# print(next_prime(20))