# --------------------------------------------------------------
# age = int(input('Enter age:  '))
# gender = input('Enter Male or Female:  ')
# if gender == 'Female':
#     print('only urban area')
# elif gender == 'Male' and 40 > age >= 20:
#     print('any')
# elif gender == 'Male' and 60 > age >= 40:
#     print('only urban area')
# else:
#     print('ERROR')

# --------------------------------------------------------------
# import random

# pc_choice = random.choice(('Rock', 'Paper', 'Scissors'))
# user_choice = input('Enter Rock or Paper or Scissors:  ')
# if user_choice == 'Rock' and pc_choice == 'Scissors' or user_choice == 'Scissors' and pc_choice == 'Paper' or user_choice == 'Paper' and pc_choice == 'Rock':
#     print('Win user')
# elif pc_choice == 'Rock' and user_choice == 'Scissors' or pc_choice == 'Scissors' and user_choice == 'Paper' or pc_choice == 'Paper' and user_choice == 'Rock':
#     print('Win pc')
# else:
#     print('Equal')
# --------------------------------------------------------------
# import random

# user = int(input('Enter your followers count:  '))
# pc = random.randint(1, 300000)
# if user + pc * 20 / 100 >= pc:
#     print('User is Bloger')
# elif pc + user * 20 / 100 >= user:
#     print('Pc is Bloger')
# --------------------------------------------------------------
# let = input('Enter letter:  ')
# number = int(input('Enter number: '))
# if let in 'aceg' and number % 2 != 0 or let in 'bdfh' and number % 2 == 0:
#     print('Black')
# else:
#     print('White')
# --------------------------------------------------------------
# --------------------- String methods -------------------------
# print('Python' > 'PJava')

# print(ord('py'))

# print(chr(1))
# --------------------------------------------------------------

# text = 'python'
# [start:stop:step]
# print(len(text))
# print(text[0])
# print(text[4])
# print(text[-2])
# print(text[2:5])
# print(text[5:2:-1])
# print(text[:6:2])
# print(text[-4:])
# print(text[:3])
# --------------------------------------------------------------


# text = 'p,y,t,h,o,n'
# text = text.replace(',', '', 3)
# print(text)
# --------------------------------------------------------------

# text = 'p,y,t,h,o,n'
# text = text.replace(',', '$')
# print(text)
# --------------------------------------------------------------


# text = 'p,y,t,h,o,n'
# text = text.split(',')
# print(text)
# text = '!'.join(text)
# print(text)

# --------------------------------------------------------------

# x = 10
# x = '10'
# print(x.isdigit())
# --------------------------------------------------------------

# x = 'Sergo'
# print(x.isalpha())
# --------------------------------------------------------------

# text = 'Sergo likes Ֆուլբոլ'
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# --------------------------------------------------------------

# print(text.isupper())
# print(text.islower())
# print(text.istitle())
# --------------------------------------------------------------
# text = 'JomolungmaEverest8848'
# print(text.isalnum())
# --------------------------------------------------------------
# text = 'Sergon siruma futbol xaxal, u chi sirum gndak'
# print(text.count('sirum', 10))
# --------------------------------------------------------------
# text = 'p$y$t$h$o$n' # B12
# text = text.replace('$', '')
# print(text) # a8
# --------------------------------------------------------------
# for number in range(0, 11, 2): # (start, stop, step)
#     if number == 6:
#         continue
#     else:
#         print(number)
# --------------------------------------------------------------
# for number in range(0, 11, 2): # (start, stop, step)
#     if number == 6:
#         break
#     else:
#         print(number)
# --------------------------------------------------------------
# for number in range(0, 11, 2): # (start, stop, step)
#     if number == 6:
#         pass
#     else:
#         print(number)
# --------------------------------------------------------------
# for i in range(10, -1, -1):
#     print(i)
# --------------------------------------------------------------
# text = 'Sergey'

# for i in range(0, len(text)):
#     print(i, text[i])
# --------------------------------------------------------------
# text = 'python'

# for i in range(0, len(text) - 1):
#     print(text[i], text[i + 1])
# --------------------------------------------------------------
# text = 'python'
# for i in text:
#     print(i)
# --------------------------------------------------------------
# text = input('Enter text:  ')
# count = 0
# for i in text:
#     if i == 'o' or i == 'O':
#         count += 1
# print(count)
# --------------------------------------------------------------
# text = input('Sharadrutyun:  ')
# dzaynavorner = 'aeiou'
# count = 0
# for i in text:
#     if i in dzaynavorner:
#         count += 1
# print(count)
# --------------------------------------------------------------
# import math

# number = int(input('Enter number:  '))
# for i in range(2, math.ceil(number ** 0.5) + 1):
#     if number % i == 0:
#         print('Baxadryal')
#         break
# else:
#     print('Parz')
# --------------------------------------------------------------
