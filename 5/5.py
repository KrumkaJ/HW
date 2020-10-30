# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while list:
    words = input('Enter text (enter space to exit): ')
    if words == ' ':
        print(my_list)
        exit()
    else:
        word = words + '\n'
        my_list.append(word)

    with open('first.txt', 'w') as my_f:
        my_f.writelines(my_list)


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('second.txt', 'r') as my_f:
    for line in my_f:
        lines = 0
        lines += 1

        flag = 0
        word = 0
        for el in line:
            if el != ' ' and flag == 0:
                word += 1
                flag = 1
            elif el == ' ':
                flag = 0
        print(f'В сторе слов {word}')

    print(f'Всего сток {lines}')

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

employees = {'Popov': 45000, 'Ivanov': 14000, 'Sidorov': 33000, 'Sorokin': 10000}

with open('third.txt', 'w') as my_f:
    for last_name, salary in employees.items():
        my_f.write(last_name + ' : ' + str(salary) + '\n')

employee = []
elem = []
with open('third.txt', 'r') as my_f:
    for line in my_f:
        el = line.split(':')
        if int(el[1]) < 20000:
            employee.append(el[0])
        elem.append(el[1])

print(f'Сотрудники с окладом меньше 20000: {employee}')
print(f'Средняя величина доходов: {sum(map(int, elem)) / len(elem)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('fourth.txt', 'r') as my_f:
    my_list = []

    for i in my_f:
        i = i.split(' ', 1)
        my_list.append(numbers[i[0]] + '  ' + i[1])
    print(my_list)

with open('fourth_new.txt', 'w') as my_f:
    my_f.writelines(my_list)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('fifth.txt', 'w') as my_f:
    my_line = '1 4 67 8 45 21'
    my_f.write(my_line)
    my_list = my_line.split()
print(sum(map(int, my_list)))

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

subjects_dict = {}
with open('sixth.txt') as my_f:
    subjects = my_f.readlines()
    for line in subjects:
        my_line = line.split(':')
        subject = my_line[0]
        # ищем в строке цифры - одну или более, и складываем
        sum_lessons = sum([int(num) for num in (re.findall('\d+', my_line[1]))])
        subjects_dict[subject] = sum_lessons
print(subjects_dict)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

profit_firm = {}
av_profit = {}
profit = 0
average_profit = 0
i = 0

with open('seventh.txt', 'r') as my_f:
    for line in my_f:
        name, form, proceeds, costs = line.split()
        profit_firm[name] = int(proceeds) - int(costs)
        if profit_firm.setdefault(name) >= 0:
            profit = profit + profit_firm.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profit / i
    av_profit = {'Average profit': round(average_profit)}
    my_list = [profit_firm, av_profit]
    print(f'Profit and loss of firms - {my_list}')

with open('seventh.json', 'w') as my_json:
    json.dump(my_list, my_json)
