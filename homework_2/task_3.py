# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить,
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# Решение через list
autumn_list = [9, 10, 11]
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]

usermonth = int(input('Введите целое число месяца: '))

if usermonth in winter_list:
    print(str(usermonth) + ' это месяц Зимы')
elif usermonth in spring_list:
    print(str(usermonth)+ ' это месяц Весны')
elif usermonth in summer_list:
    print(str(usermonth) + ' это месяц Лета')
elif usermonth in autumn_list:
    print(str(usermonth) + ' это месяц Осени')
else:
    print('введите число месяца от 1 до 12')
print('Конец программы')

# Решение через dict
months_year_dict = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима' }

# months_year_dict = {'Зима'= [1, 2, 12],'Весна' = [3, 4, 5],'Лето' = [6, 7, 8],'Осень' = [9, 10, 11] }
usermonth = int(input('Введите целое число месяца: '))

if usermonth in months_year_dict:
    print(months_year_dict.get(usermonth) + ', время года вашего месяца')
else:
    print('введите число месяца от 1 до 12')
print('Конец программы')