# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open('text_num.txt', 'w') as file:
    for _ in range(10):
        file.write(f'{random.randint(0, 10)}')

with open('text_num.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)
