# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import codecs

with codecs.open('text_1.txt', encoding="UTF-8") as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
aver_salary = sum_salary / len(employees)
print(f'Средняя зарплата = {aver_salary}')
for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')
