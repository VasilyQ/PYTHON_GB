# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

userString = input('Введите трехзначное число: ')
length = len(userString)
number = int(userString)

count = 0
sum = 0

if 99 < number < 1000:
    while count < length:
        result = number % 10
        number = number // 10
        sum = sum + result 
        count +=1
    print(f'{userString} -> {sum}')

elif -99 > number > -1000:
    number *= -1
    while count < length:
        result = number % 10
        number = number // 10
        sum = sum + result 
        count +=1
    print(f'{userString} -> {sum}')

else:
    print('число не трехначное')