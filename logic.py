# num = int(input())
# if -30 < num <= 2 or 7 < num <= 25:
#     print('Принадлежит')
# else:
#     # print('Не принадлежит')

# num = int(input())
# if (1000 <= num <= 9999) and ((num % 7 == 0) or (num % 17 == 0)):
#     print('YES')
# else:
#     print('NO')
# a, b, c = (int(input()) for i in range(3))
# if (a + b > c) and (a+c>b) and (b+c>a):
#     print('YES')
# else:
#     print('NO')

# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = (int(input()) for i in range(4))
# print('YES' if x1 == x2 or y1 == y2 else 'NO')


# def is_palindrome(word: str) -> bool:
#     if word.lower() == word[::-1].lower():
#         return True
#     return False
#
# if __name__ == '__main__':
#     string_to_check = "Redivider level rotor kayak racecar artificial intelligence"
#     elements = []
#     for el in string_to_check.split():
#         if is_palindrome(el):
#             elements.append(el)
#     print(sorted(elements, key=len, reverse=True)[0])

# n, k = (int(input()) for i in range(2))
# if n == k:
#     print("Don't know")
# else:
#     print('YES' if n < k else 'NO')

# nums = [int(input()) for i in range(3)]
# print(sorted(nums)[1])

# big = [1, 3, 5, 7, 8, 10, 12]
# mid = [4, 6, 9, 11]
# low = [2]
# month = int(input())
# print('31' if month in big else('30' if month in mid else '28'))

# dude = int(input())
# if dude < 60:
#     print('Легкий вес')
# elif 60 <= dude < 64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес')

# a, b, c = int(input()), int(input()), input()

# if c == '/':
#     if b == 0 or b == '0':
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print(int(a * b) if c == '*' else (int(a - b) if c == '-' else (int(a + b) if c == '+' else 'Неверная операция')))

# from math import sin, cos, tan, radians, pi
# x = radians(float(input()))
# print(sin(x) + cos(x) + tan(x)**2)

# x1, y1, x2, y2 = (float(input()) for i in range(4))
# res = sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print(res)
# r = float(input())
# s = lambda x: pi*x**2
# c = lambda x: 2*pi*x
# print(f'{s(r)} \n{c(r)}')

# a, b = float(input()), float(input())
# q = (a + b)/2
# w = sqrt(a * b)
# e = 2*a*b/(a + b)
# r = sqrt((a**2 + b**2)/2)
# print(q, w, e, r, sep='\n')

# from math import floor, ceil
# x = float(input())
# print(floor(x) + ceil(x))

# from math import sqrt
# a, b, c = (float(input()) for i in range(3))
#
# d = b**2 - 4 * a * c
# if d > 0:
#     x1 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
#     x2 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
#     res = f'{x1}\n{x2}'
# elif d == 0:
#     res = -b/(2 * a)
# else:
#     res = 'нет корней'
# print(res)
# res = input()
# print(f'Футбольная команда {res} имеет длину {len(res)} символов')

# symbols = [input() for i in range(3)]
# res = sorted(symbols, key=len)
# delta = len(res[0]) - len(res[1])
# if len(res[0]) + delta == len(res[1]) == len(res[2]) - delta:
#     print('YES')
# else:
#     print('NO')

# msg = input()
# if 'воскресенье' in msg or 'суббота' in msg:
#     print('YES')
# else:
#     print('NO')
# print('YES' if 'воскресенье' in input() else 'YES' if '')

# from math import log
# n, sum = int(input()), 0
# for i in range(n):
#     sum = sum + 1/(i+1)
# result = sum - log(n)
# print(result)

# n, summ = int(input()), 0
# for i in range(n):
#     if i**2 % 10 in [2, 5, 8]:
#         summ += i
# print(summ)

# from math import factorial
# print(factorial(int(input())))

# numbers = [int(input()) for i in range(10)]
# result = 1
# for i in numbers:
#     if i != 0:
#         result *= i
# print(result)

# res, num = 0, int(input())
#
# for i in range(1, num + 1):
#     if num % i == 0:
#         res += i
# print(res)

# n = int(input())
# numbers = [int(input()) for i in range(n)]
# res = sorted(numbers, reverse=True)
# print(*res[0:2], sep='\n')

# numbers = [int(input()) for i in range(10)]
# if sum(numbers) % 2 == 0 and len(set(numbers)) != 1:
#     print('YES')
# else:
#     print('NO')

# f1 = f2 = 1
# n = int(input())
# if n == 1:
#     print(1)
# elif n == 2:
#     print(1, 1, sep=' ')
# else:
#     print(f1, f2, end=' ')
#
#     for i in range(2, n):
#         f1, f2 = f2, f1 + f2
#         print(f2, end=' ')

# count = 0
# word = input()
# while word not in ('стоп', 'хватит', 'достаточно'):
#     count += 1
#     word = input()
# print(count)

# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())

# count = 0
# num = int(input())
# while 0 < num <= 5:
#     if num == 5:
#         count += 1
#     num = int(input())
#
# print(count)

# count = 0
# n = int(input())
# for i in (25, 10, 5, 1):
#     while n >= i:
#         count += 1
#         n -= i
# print(count)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# string = input()
# for i in reversed(string):
#     print(i, end='')

# string = int(input())
# print(reversed(string))

# numbers = input()
# print(f'Максимальная цифра равна {sorted(numbers)[-1]}')
# print(f'Минимальная цифра равна {sorted(numbers)[0]}')

# numbers = [int(i) for i in input()]
# res = 1
# for i in numbers:
#     res *= i
# print(sum(numbers), len(numbers), res, sum(numbers)/len(numbers), numbers[0], numbers[0] + numbers[-1], sep='\n')

# num = [int(i) for i in input()]
# if len(set(num)) > 1:
#     print('NO')
# else:
#     print('YES')

# nums = [int(i) for i in input()]
# if nums == sorted(nums, reverse=True):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# product = 1
# while n >= 10:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# n = int(input())
# for string in range(1, n + 1):
#     for i in range(5):
#         print(string, end=' ')
#     print()


# num = int(input())
#
# for i in range(1, num + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# n = int(input())
# for i in range(n//2 + 2):
#     print('*' * i)
# for i in range(n//2, 0, -1):
#     print('*' * i)

# total = 0
# for x in range(0, 100):
#     for y in range(0, 100):
#         for z in range(0, 100):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)
"""Sample Input:
3
Sample Output:
1
2 3
4 5 6"""

# n = int(input())
# count = 1
# for i in range(1, n + 1):
#     for num in range(i):
#         print(count, end=' ')
#         count += 1
#     print()

# n = int(input())
# for q in range(1, n + 1):
#     for i in range(1, q + 1):
#         print(i, end='')
#     for j in range(q - 1, 0, -1):
#         print(j, end='')
#     print()

# a, b = int(input()), int(input())
#
# numbers = dict()
# for number in range(a, b + 1):
#     count = 0
#     for i in range(1, number + 1):
#
#         if number % i == 0:
#             count += i
#         numbers[number] = count
# result = sorted(numbers.items(), key=lambda item: item[1], reverse=True)
# print(result)
# print(*result[0])


# n = int(input())
# for i in range(1, n+1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     print(i, '+' * count, sep='')

# n = input()
# first_sum = 0
# result = 0
# for i in range(len(n)):
#     first_sum += int(n[i])
#
# print(first_sum)
#
# for j in range(len(str(first_sum))):
#     result += int(first_sum[j])

# n = int(input())
# while n > 9:
#     n = n//10 + n % 10
# print(n)

# n = int(input())
# result = 1
# sum = 0
# for i in range(1, n + 1):
#     result *= i
#     sum += result
# print(sum)

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)

# n = int(input())
# print('*' * 19)
# for i in range(n-2):
#     print('*                 *')
# print('*' * 19)
'''количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).'''
# n = int(input())
# counter1, counter2, counter3, counter4, counter5, counter6 = 0, 0, 0, 0, 1, 0
# cointer2_digit = n % 10
# while n > 1:
#     last_digit = n % 10
#     if last_digit == 3:
#         counter1 += 1
#     if last_digit == cointer2_digit:
#         counter2 += 1
#     if last_digit % 2 == 0:
#         counter3 += 1
#     if last_digit > 5:
#         counter4 += last_digit
#     if last_digit > 7:
#         counter5 *= last_digit
#     if last_digit in (0, 5):
#         counter6 += 1
#     n = n // 10
#
# print(counter1, counter2, counter3, counter4, counter5, counter6, sep='\n')
while True:
    print('❤' * 100)

