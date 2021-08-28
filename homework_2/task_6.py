products =[]
counter = 1
command = ''
while command != 'stop':
    name = input('name: ')
    price = input('price: ')
    amount = input('amount: ')
    units = input('units: ')
    products.append(
        (counter, {'name': name,'price': price, 'amount': amount, 'units': units})
    )
    counter += 1
    command = input('Напишете команду "stop", чтобы завершить ввод данных')

result_list = {}
for number, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_list.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)

for key, value in result_list.items():
    result_list[key] = list(set(value))
print(result_list)