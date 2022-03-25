"""Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False


Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее
функционал."""

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     result = any(map(lambda x: x in command, ignore))
#     return result

"""Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию
о стране в формате:

<capital> is the capital of <country>, population equal <population> people.

Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
...
Для каждой страны информацию выводить на отдельной строке. """

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# result_list = zip(capitals, countries, population)
#
# [print(f'{el[0]} is the capital of {el[1]}, population equal {el[2]} people.') for el in result_list]


"""Внутри шара
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и аппликат
(z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными координатами
внутри либо на поверхности шара с центром в начале координат и радиусом R = 2

Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.

Примечание 2. Уравнение поверхности шара (сферы) имеет вид x^2+y^2+z^2 = R^2

Примечание 3. Для решения задачи используйте встроенные функции all() и zip().

Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков."""

# abscissas = map(float, input().split())
# ordinates = map(float, input().split())
# applicates = map(float, input().split())
#
#
# def is_point_inside(abs, ord, app):
#     points = zip(abs, ord, app)
#     result = all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, points))
#     return result
#
#
# print(is_point_inside(abscissas, ordinates, applicates))

"""Корректный IP-адрес
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.

В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх десятичных чисел
(октетов) со значением от 00 до 255255 (включительно), разделённых точками, например, 192.168.1.2192.168.1.2.

Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в
IP-адресе – числа со значением от 00 до 255255.

Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор символов 0-9, a-z.

Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае.

Примечание. Ведущие нули следует игнорировать:

0001 = 1
006 = 6
0213 = 213
0000 = 0
00345 = 345"""

# def is_ip_correct(text):
#     ip = text.split('.')
#     result = all(map(lambda x: 0 <= int(x) <= 255 if x.isdigit() else False, ip))
#     return result
#
#
# print(is_ip_correct(input()))

"""Интересные числа
На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции all()
для обнаружения всех целых чисел в диапазоне [a, b], которые делятся на каждую содержащуюся в них цифру без
# остатка."""
# a, b = input(), input()
#
#
# def com(num):
#     result = all(map(lambda el: int(el) and int(num) % int(el) == 0, str(num)))
#     return result
#
#
# def interesting_nums(a, b):
#     result = list(filter(com, range(int(a), int(b) + 1)))
#     return result
#
#
# print(*interesting_nums(a, b))


"""Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и
строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль."""
# import string
# password = input()
#
#
# def check_password(text):
#     terms = ['x.isdigit()', 'x in string.ascii_uppercase', 'x in string.ascii_lowercase']
#     result = list()
#
#     for rule in terms:
#         result.append(any(map(lambda x: eval(rule), text)))
#     return 'YES' if all(result) and len(text) >= 7 else 'NO'
#
#
# print(check_password(password))

"""Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе. Напишите программу с
использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число n – количество классов. Затем для каждого класса вводится блок
информации вида:

натуральное число k – количество учеников в классе;
далее вводится k строк вида: фамилия оценка."""
# result = list()
# for _ in range(int(input())):
#     students = [input() for _ in range(int(input()))]
#     result.append(any(map(lambda x: x.endswith('5'), students)))
# print('YES' if all(result) else 'NO')

"""Письмо для экзамена
Напишите функцию generate_letter(), которая будет собирать электронное письмо в соответствии с шаблоном:

To: <mail>
Приветствую, <name>!
Вам назначен экзамен, который пройдет <date>, в <time>.
По адресу: <place>.
Экзамен будет проводить <teacher> в кабинете <number>.
Желаем удачи на экзамене!

Функция должна получать на вход пять обязательных аргументов mail, name, date, time, place и два необязательных teacher,
number и возвращать текст готового письма. При отсутствии аргумента teacher учителем будет Тимур Гуев, а если нет
аргумента number, то кабинет будет 1717."""

# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     result = f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\n' \
#              f'По адресу: {place}. \nЭкзамен будет проводить {teacher} в кабинете {number}. \nЖелаем удачи на экзамене!'
#     return result
#
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))

"""Pretty print
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных
строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем
delimiter='|'."""

# def pretty_print(data, side='-', delimiter='|'):
#
#     result = delimiter + delimiter.join(map(lambda el: ' ' + str(el) + ' ', data)) + delimiter
#     top_bottom = " " + side * (len(result) - 2) + " "
#     print(f'{top_bottom}\n{result}\n{top_bottom}')


# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# files = ['duwwouy440.py', 'crocst0sse.cs', 'j9t7ga2s6x.java', 'jk4nnes4tp.py', '2spc9uqzhu.doc',
#          'qi0ujxe0c7.png', 'z5x7l1j1d8.jpg', 'i5wtdxh366.geo', 'h53s2m2p73.py', 'ojty11f02d.sx',
#          'jyjuwlvwb3.st', 'gv4940lf8m.txt', 'op38fy9m9x.docx', 'o02ltr8vbp.xlsx', 'la97gc4js4.html',
#          'lcihrp8c6l.py', 'z66y7dgfo1.py', 'ckoks0849e.csv']
#
# result = list(filter(lambda s: s.endswith('.py'), files))
#
# print(len(result))

"""Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через
разделитель (sep). Если разделитель не задан, им служит пробел."""

#
# def concat(*args, sep=' '):
#     return sep.join(str(i) for i in args)
#
#
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))

"""Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce(
). """
# from functools import reduce
#
#
# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result
#
#
# def my_product_of_odds(data):
#     filtered_data = filter(lambda x: x % 2 == 1, data)
#     result = reduce(lambda x, y: x * y, filtered_data, 1)
#     return result

"""Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все
элементы списка words, а затем печатает результат на одной строке через пробел."""

# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"', words))

"""Дан список целых чисел numbers. Допишите код после оператора распаковки (*), для удаления из списка всех
чисел-палиндромов и печати результата на одной строке через пробел."""

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

"""Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы, чтобы список sorted_numbers был
упорядочен по убыванию среднего арифметического элементов кортежей списка numbers."""

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
#            (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
# print(sorted_numbers)
"""Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной
функции, возвращая ее значение."""

# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# def call(func, *args):
#     return func(*args)
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

"""Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает
новую функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном
порядке: для функций f и g порядок применения должен выглядеть, как f(g(x))."""

# def compose(func1, func2):
#     def operation(num):
#         return func1(func2(num))
#
#     return operation
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))

"""Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций
(+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции."""

# def arithmetic_operation(operation):
#     def operands(a, b):
#         return eval(f"a {operation} b")
#     return operands
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))


"""В одну строку
Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует слова независимо
от регистра, а затем выведет их. Отсортированные слова должны выводиться на печать в исходном регистре, в каком
переданы программе на вход."""

# print(*sorted(input().split(), key=lambda x: x.lower()))

"""Гематрия слова
Гематрией слова называется сумма числовых значений входящих в него букв.

Для вычисления гематрии слова в этой задаче:

переведём слово в верхний регистр;
числовое значение буквы вычислим как код(буквы) - код(буквы A).
На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания их
гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке."""


# def gematy(word):
#     result = sum([ord(i.upper()) - ord('A') for i in word])
#     return result, word
#
#
# words = [input() for _ in range(int(input()))]
#
# print(*sorted(words, key=gematy), sep='\n')

"""Сортировка IP-адресов
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх десятичных чисел
(октетов) со значением от 00 до 255255, разделённых точками, например, 192.168.1.2192.168.1.2.

Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным
представлением."""


# ip_adreses = [[int(i) for i in input().split('.')] for _ in range(int(input()))]
# ip_adreses.sort()
# for el in ip_adreses:
#     res = '.'.join(str(i) for i in el)
#     print(res)
