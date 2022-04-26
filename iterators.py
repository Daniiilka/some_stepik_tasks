"""В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и
стандартный класс filter, но будет использовать не одну функцию, а несколько.
Пример использования:
﻿
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
"""


# class Multifilter:
#
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         if pos >= neg:
#             return True
#
#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         if pos >= 1:
#             return True
#
#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         if neg == 0:
#             return True
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         # iterable - исходная последовательность
#         self.iterable = iterable
#         # funcs - допускающие функции
#         self.funcs = funcs
#         # judge - решающая функция
#         self.judge = judge
#
#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         for el in self.iterable:
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(el):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield el
#
#
# def mul2(x):
#     return x % 2 == 0
#
#
# def mul3(x):
#     return x % 3 == 0
#
#
# def mul5(x):
#     return x % 5 == 0
#
#
# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
#
# mf = Multifilter(a, mul2, mul3, mul5)
# print(list(mf))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#
# print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))
# # [0, 30]
import itertools

"""Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только
на единицу и на само себя.

Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31,
и еще бесконечно много чисел.

Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так
как оно имеет ровно один делитель – 1.

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

Пример использования:

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
"""
# без применения теоремы Вильсона
# https://en.wikipedia.org/wiki/Wilson%27s_theorem

# def primes():
#     num = 2
#     while True:
#         counter = 0
#         for el in range(1, num + 1):
#             if num % el == 0:
#                 counter += 1
#         if counter == 2:
#             yield num
#         num += 1
#
#
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
