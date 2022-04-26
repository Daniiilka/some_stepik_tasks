"""
Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError,
ZeroDivisionError и выводит имя пойманного исключения."""


def foo():
    pass


try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


"""Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное
целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое
число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число."""


class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, el):
        if el > 0:
            super(PositiveList, self).append(el)
        else:
            raise NonPositiveError
