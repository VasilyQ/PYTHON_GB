# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


userString = input('Введите номер билета: ')
length = len(userString)/2
number = int(userString)
result = number // 1000

sum = 0
count = 0

while count < length:
    index = number % 10
    number = number // 10
    sum += index
    count += 1

sum2 = 0
count = 0
while count < length:
    index = result % 10
    result = result // 10
    sum2 += index
    count += 1


if sum2 == sum:
    print('Yes')

else:
    print('No')