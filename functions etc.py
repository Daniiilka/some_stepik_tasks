"""Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации."""
# l = [1, 2, 3, 4, 5, 6]
#
#
# def modify_list(l):
#     new_list = []
#     for i in reversed(range(len(l))):
#         if l[i] % 2 == 0:
#             new_list.append(l[i])
#     for i in range(len(new_list)):
#         new_list[i] = int(new_list[i] // 2)
#     l[:] = [new_list]
#
#
# def another_modify_list(l):
#     for i in reversed(range(len(l))):
#         if l[i] % 2 == 0:
#             l[i] //= 2
#         else:
#             del l[i]
#
#
# modify_list(l)
# -------------------------------------------------------
# set() множества, dict, {} множества
"""Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и
valuevalue.

Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key
нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}"""

# d = {}
#
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2*key in d:
#         d[key * 2] += [value]
#     else:
#         d[key * 2] = [value]
#
#
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}'''

"""Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
 вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз."""

# list = input().lower().split()
# for i in set(list):
#     print(f"{i} {list.count(i)}")
#
"""Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
 Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас
 получится, надо отправить в качестве ответа на эту задачу."""

# with open('dataset_3363_2.txt') as data:
#     di = {}
#
#     for line in data:
#         for i in range(len(line)):
#             num = ''
#             if line[i].isalpha():
#                 key = line[i]
#             elif line[i].isdigit() and line[i + 1].isdigit():
#                 num = str(line[i]) + str(line[i+1])
#
#             elif line[i].isdigit() and line[i + 1].isalpha():
#                 num = str(line[i])
#
#             di[key] = num
#
# # print(di)
# import re
# with open('dataset_3363_2 (2).txt','r+') as f:
#     a = re.split(r"(\d+)",f.readline())[:-1]
#     result = ''.join([y * int(x) for x,y in zip(a[1::2],a[::2])])
#     print(result)
#     f.seek(0)
#     f.write(result)
"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми."""
# from collections import Counter
#
#
# with open('dataset_3363_3 (2).txt') as file:
#
#     c = Counter(file.read().lower().split())
#
#     print(c.most_common(1)[0][0], c.most_common(1)[0][1])

"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные
значения, разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со
средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
"""

# math, phys, rus = [], [], []
# math_sum, phys_sum, rus_sum = 0, 0, 0
#
# with open('dataset_3363_4 (3).txt', encoding='utf-8') as file:
#     for line in file:
#         var = [line.strip().split(';')]
#
#         for num in var:
#             math.append(int(num[1]))
#             phys.append(int(num[2]))
#             rus.append(int(num[3]))
#
#             with open('result', 'a') as result:
#                 mid = (int(num[1]) + int(num[2]) + int(num[3]))/3
#
#                 result.write(str(round(mid, 9)))
#                 result.write('\n')
#
#     with open('result', 'a') as result:
#         result.write(f"{round(sum(math)/len(math), 9)} {round(sum(phys)/len(phys), 9)} {round(sum(rus)/len(rus),9)}")
