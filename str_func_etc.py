# s = 'abc'
#
# for i in range(1, len(s) + 1):
#     print(s[-i])

# fio = [input() for i in range(3)]
# print(fio[1][0], fio[0][0], fio[2][0], sep='')

# string = input()
# result = 0
# for i in string:
#     result += int(i)
# print(result)

# string = input()
# result = False
# for i in string:
#     if i.isdigit():
#         result = True
# print('Цифр нет' if result == False else 'Цифра')

# string = input()
# plus, stars = 0, 0
# for i in string:
#     if i == '+':
#         plus += 1
#     elif i == '*':
#         stars += 1
# print(f'Символ + встречается {plus} раз\nСимвол * встречается {stars} раз')

# s = input()
# counter = 0
# for i in range(1, len(s) + 1):
#     if s[i] == s[i + 1]:
#         counter += 1
# print(counter)

# s = input()
# c1, c2 = 0, 0
# for i in s.lower():
#     if i in 'ауоыиэяюёе':
#         c1 += 1
#     elif i in 'бвгджзйклмнпрстфхцчшщ':
#         c2 += 1
# print(f'Количество гласных букв равно {c1}\nКоличество согласных букв равно {c2}')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# s = input()
# if s == s[::-1]:
#     print('YES')
# else:
#     print('NO')

'''общее количество символов в строке;
исходную строку повторенную 3 раза;
первый символ строки;
первые три символа строки;
последние три символа строки;
строку в обратном порядке;
строку с удаленным первым и последним символом.'''
# s = input()
# print(len(s), s*3, s[0], s[:3], s[-3:], s[::-1], s[1:-1], sep='\n')

'''третий символ этой строки;
предпоследний символ этой строки;
первые пять символов этой строки;
всю строку, кроме последних двух символов;
все символы с четными индексами;
все символы с нечетными индексами;
все символы в обратном порядке;
все символы строки через один в обратном порядке, начиная с последнего.'''

# s = input()
# print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], sep='\n')

# s = input()
# a = s[:len(s) - len(s)//2]
# b = s[len(s) - len(s)//2:len(s)]
# print(b + a)

'''Англо-русский словарик:
capitalize — писать прописными буквами, закрепить.
swapcase — обменять регистр. swap — гл. обмениваться, case — случай, регистр, падеж, дело, расследование...
title — заголовок, титул.
lower — нижний.
upper — верхний.
'''

# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')

# s = input()
# count = 0
# for i in s:
#     if i == i.lower() and i.isalpha():
#         count += 1
# print(count)

# s = input().lower()
# print('Аденин: ' + str(s.count("а")), 'Гуанин: ' + str(s.count("г")), 'Цитозин: ' + str(s.count("ц")), 'Тимин: ' + str(s.count("т")), sep='\n')

# n = int(input())
# count = 0
# for i in range(n):
#     if input().count('11') >= 3:
#         count += 1
# print(count)

# s = input()
# count = 0
# for i in s:
#     if i.isdigit():
#         count += 1
# print(count)

# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# s = input()
# count_max = 0
# letter = ''
# for i in s:
#     if s.count(i) >= count_max:
#         count_max = s.count(i)
#         letter = i
# print(letter)

# string = input()
# if string.count('f') == 1:
#     print(string.find('f'))
# elif string.count('f') > 1:
#     print(string.find('f'), string.rfind('f'))
# else:
#     print('NO')

# string = input()
# print(string[:string.find('h')] + string[string.rfind('h') + 1:])

# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format('2010', '10k', 'Bitcoin')
#
# print(s)
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# result = [letters[i] * (i + 1) for i in range(0, len(letters))]
# print(result)

# n = int(input())
# result = []
# for i in range(1, n + 1):
#     result.append(i ** 3)
# print(result)
# # ---------------------------------------------------
# result = [int(input()) ** 3 for i in range(1, int(input()) + 1)]
# print(result)

# final = int(input())
# result = [i for i in range(1, final + 1) if final % i == 0]
# print(result)

# n = int(input())
# first_list = [int(input()) for i in range(1, n + 1)]
# second_list = []
# for element in range(len(first_list) - 1):
#     second_list.append(first_list[element] + first_list[element + 1])
# print(second_list)

# n = int(input())
# f_lst = [int(input()) for i in range(n)]
# del f_lst[1::2]
# print(f_lst)

# n = int(input())
# res = [input() for i in range(n)]
# k = int(input())
# for i in range(len(res)):
#     print(res[i][k - 1: k], end='')

# n = int(input())
# res = list()
# for i in range(n):
#     res.extend(input())
# print(res)
'''f(x) = x^2 + 2x + 1'''
# numbers = [int(input()) for i in range(int(input()))]
# print(*numbers, sep='\n')
# print()
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] ** 2 + numbers[i] * 2 + 1
#
# print(*numbers, sep='\n')

# n = int(input())
# nums = [int(input()) for i in range(n)]
# check_nums = sorted(nums)
#
# for num in nums:
#     if num == check_nums[0] or num == check_nums[-1]:
#         nums.remove(num)
#
# print(*nums, sep='\n')

# n = int(input())
# row = [input() for i in range(n)]
# result = []
# for word in row:
#     if word not in result:
#         result.append(word)
# print(*result, sep='\n')

# n = int(input())
# sentences = [input() for _ in range(n)]
# check = int(input())
# key = [input().lower() for _ in range(check)]
# for sentence in sentences:
#     count = 0
#     for word in key:
#         if word in sentence.lower():
#             count += 1
#     if count == len(key):
#         print(sentence)

# negatives, zeroes, positives, numbers = [], [], [], [int(input()) for i in range(int(input()))]
# for number in numbers:
#     if number < 0:
#         negatives.append(number)
#     elif number == 0:
#         zeroes.append(number)
#     else:
#         positives.append(number)
# print(*negatives, *zeroes, *positives, sep='\n')

# s = input().split('.')
# flag = True
# for i in s:
#     if 0 > int(i) or int(i) > 255:
#         flag = False
# print('ДА' if flag == True else 'НЕТ')

# res = input()
# add = input()
# print(add.join(res))

# nums = [int(i)**3 for i in input().split()]
# print(*nums)

# string = [i for i in input() if i.isdigit()]
# print(*string, sep='')

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
     -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
     -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
     -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)


# реализация алгоритма сортировки выбором
# for i in range(n):
#     minimum = i
#     for j in range(i + 1, n):
#         if a[j] < a[minimum]:
#             minimum = j
#     a[minimum], a[i] = a[i], a[minimum]
# print(a)

# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
# draw_box()


# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# draw_triangle()


# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base//2 + 2):
#         print(fill * i)
#     for j in range(base//2, 0, -1):
#         print(fill * j)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# объявление функции
# def print_digit_sum(num):
#     result = 0
#     for i in num:
#         result += int(i)
#     print(result)
#
# # считываем данные
# n = input()
#
# # вызываем функцию
# print_digit_sum(n)


# def convert_to_miles(km):
#     mile = km * 0.6214
#     return mile


# def get_days(month):
#     months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return months[month - 1]
#
# print(get_days(2))


# объявление функции
# def merge(list1, list2):
#     return sorted(list1 + list2)
#
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merge(nums):
#     result = sorted(nums)
#     return result
#
# n = int(input())
# nums = []
# for i in range(n):
#     nums += [int(i) for i in input().split()]
#
# print(*quick_merge(nums))


# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# # объявление функции
# def get_next_prime(num):
#     while not is_prime(num + 1):
#         num += 1
#         continue
#     return num + 1


# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))
'''число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.'''
# объявление функции


def is_valid_password(password):
    palindrome, simple, even = False, False, False
    password = password.split(':')
    if password[0] == password[0][::-1]:
        palindrome = True
        


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))