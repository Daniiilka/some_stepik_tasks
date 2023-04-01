"""
Реализуйте функцию hide_card(), которая принимает один аргумент:

card_number — строка, представляющая собой корректный номер банковской карты
из 1616 цифр, между которыми могут присутствовать символы пробела
Функция должна заменять первые 1212 цифр в строке card_number на символ *
и возвращать полученный результат. Если между цифрами в номере имелись
символы пробела, их следует удалить.
"""
import collections


def hide_card(number):
    number_without_spaces = number.replace(" ", "")
    result = ""
    count = 0
    if len(number_without_spaces) == 16:
        for num in number_without_spaces:
            if count <= 12:
                result += "*"
            else:
                result += num
            count += 1
    return str(result)


"""
Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа 
из списка numbers, имеющие ту же четность, что и первый элемент этого списка."""


def same_parity(numbers):
    try:
        first_even = True if numbers[0] % 2 == 0 else False
        result = [el for el in numbers if el % 2 != first_even]
    except IndexError:
        result = numbers
    return result


"""
Функция is_valid()
Будем считать, что PIN-код является корректным, если он удовлетворяет 
следующим условиям:

состоит из 44, 55 или 66 символов
состоит только из цифр (0-90−9)
не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если строка string представляет 
собой корректный PIN-код, или False в противном случае."""


def is_valid(string: str):
    return (4 <= len(string) <= 6) and string.isdigit()


"""Реализуйте функцию print_given(), которая принимает произвольное 
количество позиционных и именованных аргументов и выводит все переданные 
аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться 
каждая на отдельной строке, в следующем формате:

для позиционных аргументов:
<значение аргумента> <тип аргумента>
для именованных аргументов:
<имя переменной> <значение аргумента> <тип аргумента>"""


def print_given(*args, **kwargs):
    result = []
    for el in args:
        print(el, type(el))
    for name, value in kwargs.items():
        result.append([name, value, type(value)])
    [print(*el) for el in sorted(result)]


"""
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах 
в этой строке совпадает
"""


def convert(string: str):
    count_of_lower = sum([1 for el in string if el.islower() and el.isalpha()])
    count_of_upper = sum([1 for el in string if el.isupper() and el.isalpha()])
    return string.lower() if count_of_lower >= count_of_upper else string.upper()


"""
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в 
следующем порядке:

word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка 
words, которые представляют анаграмму слова word. Если список words пуст или 
не содержит анаграмм, функция должна вернуть пустой список."""


def filter_anagrams(word, words: list):
    words = list(filter(lambda el: (sorted(el) == sorted(word)), words))
    return words


"""
В различных социальных сетях существуют системы лайков, которые в 
зависимости от количества людей, оценивших запись, показывают 
соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:

names — список имён
Функция должна возвращать строку в соответствии с примерами ниже, 
содержание которой зависит от количества имён в списке names.

Приведенный ниже код:

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 
'Гвидо', 'Марк']))
должен выводить:

Никто не оценил данную запись
Тимур оценил(а) данную запись
Тимур и Артур оценили данную запись
Тимур, Артур и Руслан оценили данную запись
Тимур, Артур и 2 других оценили данную запись
Тимур, Артур и 3 других оценили данную запись
Тимур, Артур и 6 других оценили данную запись
"""


def likes(s):
    result = (
        "'Никто не оценил'",
        "f'{s[0]} оценил(а)'",
        "f'{s[0]} и {s[1]} оценили'",
        "f'{s[0]}, {s[1]} и {s[2]} оценили'",
        "f'{s[0]}, {s[1]} и {len(s) - 2} других оценили'",
    )
    return eval(result[len(s) if len(s) <= 3 else 4]) + " данную запись"


"""Реализуйте функцию index_of_nearest(), которая принимает два аргумента в 
следующем порядке:

numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к 
числу number и возвращать его индекс. Если список numbers пуст, функция 
должна вернуть число -1−1.

Примечание 1. Если в функцию передается список, содержащий несколько 
чисел, одновременно являющихся ближайшими к искомому числу, функция 
должна возвращать наименьший из индексов ближайших чисел."""


def index_of_nearest(numbers: list, number: int):
    if len(numbers) < 1:
        return -1
    numbers_difference = [abs(el - number) for el in numbers]
    min_diff = min(numbers_difference)
    nearest = numbers_difference.index(min_diff)
    return nearest


"""
Реализуйте функцию spell(), которая принимает произвольное количество 
позиционных аргументов-слов и возвращает словарь, ключи которого — первые 
буквы слов, а значения — максимальные длины слов на эту букву.
"""


def spell(*words_list):
    main_letter = [word[0].lower() for word in words_list]
    max_length = dict.fromkeys(main_letter, 0)
    for word in words_list:
        if len(word) > max_length[word[0].lower()]:
            max_length[word[0].lower()] = len(word)
    return max_length


"""
Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего 
существительного из кортежа declensions и количества amount, в следующем формате:

<количество> <существительное>
"""


def choose_plural(amount: int, declensions: tuple):
    if amount % 10 == 1 and amount % 100 != 11:
        declension = declensions[0]
    elif amount % 10 in (2, 3, 4) and amount % 100 not in (12, 13, 14):
        declension = declensions[1]
    else:
        declension = declensions[2]
    return f"{amount} {declension}"


"""
Реализуйте функцию get_biggest(), которая принимает один аргумент:

numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка 
numbers. Если список numbers пуст, функция должна вернуть число -1−1."""


def get_biggest(numbers: list):
    # todo
    pass


"""
Напишите программу, которая вычисляет минимальное расстояние, которое 
потребуется пройти Тимуру, чтобы посетить оба магазина и вернуться 
домой. Тимур всегда стартует из дома. Он должен посетить оба магазина, 
перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой. 
При этом его совершенно не смутит, если ему придётся посетить один и 
тот же магазин или пройти по одной и той же дорожке более одного раза.
Единственная его задача — минимизировать суммарное пройденное расстояние.
"""


def get_min_path():
    d1 = int(input())
    d2 = int(input())
    d3 = int(input())
    path1 = d1 + d2 + d3
    path2 = d1 + d1 + d2 + d2
    path3 = d1 + d3 + d3 + d1
    path4 = d2 + d3 + d3 + d2
    print(min(path2, path1, path4, path3))


"""
В русском и английском языках есть буквы, которые выглядят одинаково. 
Вот список английских букв "AaBCcEeHKMOoPpTXxy", а вот их русские 
аналоги "АаВСсЕеНКМОоРрТХху". Напишите программу, которая для трёх 
букв из данных списков букв определяет, русские они, английские или 
и те и другие (смесь русских и английских букв)."""


def similar_letters():
    en, ru = "AaBCcEeHKMOoPpTXxy", "АаВСсЕеНКМОоРрТХху"
    letters = [str(input()) for _ in range(3)]
    if letters[0] in en and letters[1] in en and letters[2] in en:
        print("en")
    elif letters[0] in ru and letters[1] in ru and letters[2] in ru:
        print("ru")
    else:
        print("mix")


"""
Дана последовательность натуральных чисел от 11 до nn. Напишите 
программу, которая сначала располагает в обратном порядке часть 
элементов этой последовательности от элемента с номером XX до 
элемента с номером YY, а затем от элемента с номером AA до элемента 
с номером BB.
"""


def reverse_nums():
    # 9 2 5 6 9

    n, x, y, a, b = [int(el) for el in input().split()]
    sequence = list(range(1, n + 1))
    first_reverse = list(reversed(sequence[x - 1: y]))
    second_reverse = list(reversed(sequence[a - 1: b]))

    print(*(sequence[: x - 1] + first_reverse + second_reverse + sequence[b:]))


"""Более одного
Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются 
в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом. 
Числа должны быть расположены в порядке возрастания и не должны повторяться."""


def counter():
    nums = list(int(el) for el in input().split())
    uniq_nums = set(el for el in nums if nums.count(el) > 1)
    return list(uniq_nums)


"""Максимальная группа
Назовем набор различных натуральных чисел группой. Например: (13, 4, 22, 40)(13,4,22,40). Тогда длиной группы будем 
считать количество чисел в группе. Например, длина группы (13, 4, 22, 40)(13,4,22,40) равна 44.

Дана последовательность натуральных чисел от 11 до nn включительно. Напишите программу, которая группирует все числа 
данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел."""


def max_group(n):
    nums = list(range(1, n + 1))
    result_groups = []
    for index in range(1, len(nums) + 1):
        result_groups.append([el for el in nums if sum(map(int, list(str(el)))) == index])
    return len(sorted(result_groups, key=len)[-1])


"""Трудности перевода
Зачастую переводить сериалы, не теряя изначальный смысл, невозможно, особенно за счет игр слов. Сумасшедший режиссер 
хочет снять сериал, в котором бы в целях эксперимента задействовал как можно больше языков, чтобы пользоваться красотой 
каждого из них. Тем не менее если задействовать слишком много языков, то сериал станет непонятен абсолютно всем, поэтому 
режиссер достает случайных людей на улице и спрашивает их, какие языки они знают, таким образом он будет использовать 
языки которые знают все из них.

Напишите программу, которая определяет, какие языки будут использоваться в сериале.

"""


def translation_issues():
    n = int(input())
    user_languages = []
    for _ in range(n):
        user_languages.append(list(el.strip(' ') for el in input().split(',')))
    result = sorted(set.intersection(*map(set, user_languages)))
    print(', '.join(result) if len(result) > 0 else 'Сериал снять не удастся')


"""Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют 
одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться."""


def transform(word):
    vowels = 'ауоыиэяюёе'
    transformed = ''
    for el in word:
        if el in vowels:
            transformed += '1'
        else:
            transformed += '0'
    return transformed


def similar_words():
    init_word = str(input())
    transformed_init = transform(init_word)
    transformed_init = transformed_init[:transformed_init.rfind('1')]

    count = int(input())
    words = [str(input()) for _ in range(count)]
    for word in words:
        transformed_word = transform(word)
        if transformed_word[:transformed_word.rfind('1')] == transformed_init:
            print(word)


"""В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz, 
например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено 
приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий — 
timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде 
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы."""


def corporate_mail():
    mail_service = '@beegeek.bzz'
    n = int(input())
    mail_list = [str(input()).replace(mail_service, '') for _ in range(n)]
    find_n = int(input())
    find_mail = [str(input()) for _ in range(find_n)]


"""Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения, 
разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит 
полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом 
порядке названий расширений, файлы в группах — в лексикографическом порядке их имен."""


def sum_size(size: list):
    from decimal import Decimal
    size_file = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
    size_in_bytes = []
    for el in size:
        size_in_bytes.append(Decimal(int(size_file[el[1]]) * int(el[0])), )
    sum_size_bytes = sum(size_in_bytes)
    if sum_size_bytes > 1023:
        size_in_kb = round(sum_size_bytes/1024)
        actual_size = f'{size_in_kb} KB'
        if size_in_kb > 1023:
            size_in_mb = round(size_in_kb/1024)
            actual_size = f'{size_in_mb} MB'
            if size_in_mb > 1023:
                size_in_gb = round(size_in_mb/1024)
                actual_size = f'{size_in_gb} GB'
    return actual_size


def sort_files():

    with open('files.txt', 'r') as data:
        files_list = data.readlines()
    files_dict = dict()
    for raw_file in files_list:
        raw_file_info = raw_file.split()
        file_name, file_type = raw_file_info[0].split('.')
        size = raw_file_info[1:]

        if file_type not in files_dict:
            files_dict[file_type] = {}
            files_dict[file_type]['names'] = file_name
            files_dict[file_type]['size'] = [size]
        else:
            files_dict[file_type]['names'] += f' {file_name}'
            files_dict[file_type]['size'].append(size)
    for file_type in sorted(files_dict):
        [print(f'{name}.{file_type}') for name in sorted(files_dict[file_type]['names'].split())]
        print('----------')
        sum_suze = sum_size(files_dict[file_type]["size"])
        print(f'Summary: {sum_suze}')
        print()


if __name__ == "__main__":
    sort_files()
