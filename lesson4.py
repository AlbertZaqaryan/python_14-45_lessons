# import random

# nums = input('write 5 numbered string ')
# a = str(random.randint(1, 10))
# print(a in nums)

# import math

# n = int(input('Enter your number: '))
# print(math.factorial(n))


# tobac = int(input('Enter tobac in gramms:  '))
# print(tobac // 20)

# ----------------------------------------------------------------
# ------------------------ if, elif, else ------------------------
# x = int(input('Enter number1:   '))
# y = int(input('Enter number2:   '))
# if x >= y:
#     print('X is max!!')
#     if x > 10:
#         print('X > 10')



# x = int(input('Enter number1:   '))
# y = int(input('Enter number2:   '))

# a = int(input('Enter number1:   '))
# b = int(input('Enter number2:   '))
# if x > y:
#     print('X is max!!!')
# elif x == y:
#     print('Equal!!!')
# else:
#     print('Y is max!!!')



# tar = input('Mutqagreq tar:  ')
# if tar.isupper():
#     print('Mecatar')
# else:
#     print('Poqratar')
    

# x = input('Enter x: ')
# if x.isdigit():
#     print('Number')
# elif x.isalpha():
#     print('Letter')
# else:
#     print('Char')

# text = input('Enter text: ')
# if 'a' in text and 'b' in text and 'k' not in text:
#     print('Ok')
# else:
#     print(':(')

# n = int(input('Enter number: '))
# if n % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
# ----------------------------------------------------------------
# import random

# pc_points = 0
# user_points = 0
# pc = random.randint(0, 5)
# user = int(input('Enter number in range(0-5):   '))
# if user == pc: # user = 1, pc = 0
#     user_points += 1
#     print(f'---->Win user<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0-5):   '))
#     if user == pc: # user = 2, pc = 0 END GAME WIN USER
#         user_points += 1
#         print(f'---->Win user<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#         print('--------------- END GAME WIN USER!!! ----------------')
#     else: # user = 1, pc = 1
#         pc_points += 1    
#         print(f'---->Win pc<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0-5):   '))
#         if user == pc: # user = 2, pc = 1 END GAME WIN USER
#             user_points += 1
#             print(f'---->Win user<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#             print('--------------- END GAME WIN USER!!! ----------------')
#         else: # user = 1, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---->Win pc<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#             print('--------------- END GAME WIN PC!!! ----------------')
# else: # user = 0, pc = 1
#     pc_points += 1
#     print(f'---->Win pc<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#     pc = random.randint(0, 5)
#     user = int(input('Enter number in range(0-5):   '))
#     if user == pc: # user = 1, pc = 1
#         user_points += 1
#         print(f'---->Win user<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#         pc = random.randint(0, 5)
#         user = int(input('Enter number in range(0-5):   '))
#         if user == pc: # user = 2, pc = 1 END GAME WIN USER
#             user_points += 1
#             print(f'---->Win user<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#             print('--------------- END GAME WIN USER!!! ----------------')
#         else: # user = 1, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---->Win pc<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#             print('--------------- END GAME WIN PC!!! ----------------')
#     else: # user = 0, pc = 2 END GAME WIN PC
#         pc_points += 1
#         print(f'---->Win pc<-----\nUser = {user}, Pc = {pc}\nUser points = {user_points}, Pc points = {pc_points}')
#         print('--------------- END GAME WIN PC!!! ----------------')
# ----------------------------------------------------------------
# dog_age = int(input('Enter dog age:  '))
# if 0 < dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# elif dog_age > 2:
#     print('Human age = ', 21 + (dog_age - 2) * 4)
# else:
#     print('Error')

# dzaynavorner = 'aeiou'
# tar = input('Mutqagreq tar: ')
# if tar in dzaynavorner:
#     print('Dzaynavor')
# else:
#     print('Baxadzayn')


# x = '$'
# y = '%'
# print(x + y)


# year = int(input('Enter year: '))
# if year % 4 == 0:
#     print('Leep')
# else:
#     print('No Leep')


