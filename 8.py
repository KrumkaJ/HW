# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_form):
        self.date_form = str(date_form)

    @classmethod
    def my_data(cls, date_form):
        my_date_form = []

        for i in date_form.split():
            if i != '-': my_date_form.append(i)

        return int(my_date_form[0]), int(my_date_form[1]), int(my_date_form[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Верная дата'
                else:
                    return f'Неверная дата'
            else:
                return f'Неверная дата'
        else:
            return f'Неверная дата'


date = Date('21 - 8 - 2000')
print(Date.my_data('2 - 12 - 1999'))
print(date.my_data('24 - 7 - 2010'))
print(Date.validation(19, 1, 2022))
print(Date.validation(7, 8, 1995))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class ZeroError(Exception):
    def __init__(self, txt_error):
        self.txt = txt_error


arg1 = int(input('Введите первое число: '))
arg2 = int(input('Введите второе число: '))


try:
    if arg2 == 0:
        raise ZeroError('На ноль делить нельзя!')

except ZeroError as error_txt_msg:
    print(error_txt_msg)

else:
    print(arg1 / arg2)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
# сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.


class ErrorOnlyNumbers(Exception):
    def __init__(self, text_error):
        self.txt = text_error


my_list = []
while True:
    number = input('Введите число, для выхода введите "stop": ')
    try:
        if number.isdigit():
            my_list.append(number)
        elif number == "stop":
            print(my_list)
            break
        else:
            raise ErrorOnlyNumbers('Ошибка. Введите число.')
    except ErrorOnlyNumbers as error_txt_msg:
        print(error_txt_msg)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    def __init__(self):
        self.addition = {}

    def add_to(self, equipment):
        self.addition.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self.addition[name]:
            self.addition.setdefault(name).pop(0)


class OfficeEquipment:
    def __init__(self, quantity, price, brand, country_of_origin):
        self.quantity = quantity
        self.price = price
        self.brand = brand
        self.country_of_origin = country_of_origin
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.quantity} {self.price} {self.brand} {self.country_of_origin}'

    def work(self):
        print('Функциональность')


class Printer(OfficeEquipment):
    def __init__(self, quantity, price, brand, country_of_origin):
        super().__init__(quantity, price, brand, country_of_origin)

    def work(self):
        print('Печать документов')


class Scanner(OfficeEquipment):
    def __init__(self, quantity, price, brand, country_of_origin):
        super().__init__(quantity, price, brand, country_of_origin)

    def work(self):
        print('Скан документов')


class Xerox(OfficeEquipment):
    def __init__(self, quantity, price, brand, country_of_origin):
        super().__init__(quantity, price, brand, country_of_origin)

    def work(self):
        print('Ксерокопия документов')


class Shredder(OfficeEquipment):
    def __init__(self, quantity, price, brand, country_of_origin):
        super().__init__(quantity, price, brand, country_of_origin)

    def work(self):
        print('Уничтожение документов')


warehouse = Warehouse()
# добавляем на склад
printer = Printer(1, 5000, 'HP', 'China')
warehouse.add_to(printer)
scanner = Scanner(1, 30000, 'Canon', 'Japan')
warehouse.add_to(scanner)
scanner = Scanner(1, 25000, 'HP', 'Japan')
warehouse.add_to(scanner)
xerox = Xerox(1, 15000, 'Xerox Corporation', 'Vietnam')
warehouse.add_to(xerox)
xerox = Xerox(1, 15000, 'Xerox Corporation', 'China')
warehouse.add_to(xerox)
shredder = Shredder(1, 8000, 'Cactus', 'China')
warehouse.add_to(shredder)
# выводим склад
print(warehouse.addition)
# забираем с склада и выводим склад
warehouse.extract('Scanner')
print()
print(warehouse.addition)
warehouse.extract('Xerox')
print()
print(warehouse.addition)


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.sumx = self.x + obj.x
        self.sumy = self.y + obj.y

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y


a = ComplexNumber(5, 6)
b = ComplexNumber(8, 9)
a + b
a * b
print(f'Сумма: {a.sumx}+{a.sumy}i')
print(f'Произведение: {a.multx}+{a.multy}i')
