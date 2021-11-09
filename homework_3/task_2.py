# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def users(name, surname, year, city, mail, phone):
    print(f'{name} {surname} {year} {city} {mail} {phone}')


name = input('name: ')
surname = input('surname: ')
year = input('year: ')
city = input('city: ')
mail = input('mail: ')
phone = input('phone: ')

users(name, surname, year, city, mail, phone)
