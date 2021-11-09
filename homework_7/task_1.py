"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        s = ""
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                s += f'{self.nums[i][j]:02} '
            s += "\n"
        return s

    def __add__(self, other):
        nums = [
            [self.nums[i][j] + other.nums[i][j] for j in range(len(self.nums[i]))]
            for i in range(len(self.nums))]
        return Matrix(nums)


a = Matrix([[randint(0, 10) for _ in range(10)] for _ in range(10)])
b = Matrix([[randint(0, 10) for _ in range(10)] for _ in range(10)])
print(a)
print(b)
print(a + b)
