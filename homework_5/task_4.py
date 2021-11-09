# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('text_2.txt') as file, open('new_text_2.txt', 'w') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_num = num_dict.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_num)}')
