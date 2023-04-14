# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))

degree = 0
count = 1
while degree < n:
    degree = 2 ** count
    count += 1
    print(degree)