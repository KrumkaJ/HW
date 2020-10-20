# №1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = ['Food', 6785, True, 5.7]

for element in some_list:
    print(element, type(element))

# №2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

numbers = int(input('Введите количество элементов в списке: '))

i = 0
members = []
element = 0

while i < numbers:
    members.append(input(f'Введите элемент списка '))
    i += 1

print(list(members))

for index in range(int(len(members)/2)):
    members[element], members[element + 1] = members[element + 1], members[element]
    element += 2

print(members)

# №3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# список
season_list = ['winter', 'spring', 'summer', 'autumn']

month = int(input('Введите номер месяца '))

if month == 1 or month == 2 or month == 12:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
else:
    print('Error')

# словарь
season_dict = {'season_1' : 'winter', 'season_2' : 'spring', 'season_3' : 'summer', 'season_4': 'autumn'}

month = int(input('Введите номер месяца '))

if month == 1 or month == 2 or month == 12:
    print(season_dict['season_1'])
elif month == 3 or month == 4 or month == 5:
    print(season_dict['season_2'])
elif month == 6 or month == 7 or month == 8:
    print(season_dict['season_3'])
elif month == 9 or month == 10 or month == 11:
    print(season_dict['season_4'])
else:
    print('Error')

# №4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Введите несколько слов через пробел: ')

my_list = my_str.split()

for i, el in enumerate(my_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) {el}")

# #5 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_list = [9, 7, 7, 4, 2]
print(my_list)

number = int(input('Введите натуральное число: '))

for i in range(len(my_list)):
    if my_list[i] == number:
        my_list.insert(i + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
        break
    elif my_list[1] < number:
        my_list.insert(1, number)
        break
    elif my_list[3] < number:
        my_list.insert(3, number)
        break
    elif my_list[4] < number:
        my_list.insert(4, number)
        break
    elif my_list[4] > number:
        my_list.insert(4 + 1, number)
        break

print(my_list)

# №6 Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]

# Структурв данныъ "Товары"
goods = int(input('Введите количество продуктов, которое вы хотите купить: '))
number = 1
goods_list = []
goods_dict = []

while number <= goods:
    my_dict = {
        'Название': input('Ведите название товара: '),
        'Цена': input('Введите цену товара: '),
        'Kоличество': input('Введите количество товара: '),
        'Ед': input("Введите единицу измерения товара: ")
    }
    goods_dict = my_dict
    goods_list.append((number, goods_dict))
    number += 1

print(goods_list)

# Аналитика товаров
analytics = {}

for good in goods_list:
    for key, val in good[1].items():
        if key in analytics:
            analytics[key].append(val)
        else:
         analytics[key] = [val]

print(analytics)
