# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    nums_sum = num1 + num2 + num3
    return nums_sum - min((num1, num2, num3))

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
result = my_func(num1, num2, num3)

print(result)

