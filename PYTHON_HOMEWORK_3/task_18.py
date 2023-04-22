# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элементк заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

list = [random.randint(-100, 100) for i in range(10)]
# list = [1, 8, 5, 5, 125, 9, 15, 16]
print(*list)
result = 0
number = int(input('Введите число: '))
min = abs(list[0] - number)
for i in list:
    if abs(i - number) < min:
        min = abs(i - number)
        result = i
print(result)





    


