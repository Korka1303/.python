# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('text.txt', 'w') as file:
    input_lini = input('Текст : \n')
    while input_lini:
        file.write(f'{input_lini}\n')
        input_lini = input('Текст : \n')