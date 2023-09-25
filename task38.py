# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os

def user_inform():
    surname = input('введите фамилию ')
    name = input('введите имя ')
    patronymic = input('введите отчество ')
    tel = input('введите номер телефона ')
    return f'{surname} {name} {patronymic} {tel}\n'

def add_file(route):
    with open('file1.txt','a') as file:
        file.write(user_inform())


def find_el(route, search_input):
    with open('file1.txt', 'r') as file:
        lst_1=file.readlines()
        flag1 = False
        result = '\n'
        for line in lst_1:
            if search_input in line:
                result += line
                flag1 = True
        if not flag1:
            result = 'Извините, такой записи нет.'
    return result

def show_all(route):
    with open('file1.txt','r') as file:
        return file.read()

def del_line(route, searh_input):
    with open('file1.txt', 'r') as file:
        lst_1 = file.readlines()
        lst_2 = []
        for line in lst_1:
            if searh_input not in line:
                lst_2.append(line)

    with open('file1.txt', 'w') as file:
        result = file.writelines(lst_2)

    return result

#def get_user_intention():
text_zapros = 'Введите номер команды, которую хотите выполнить.\n' \
    '1. Записать новые данные в файл?\n' \
    '2. Найти конкретную запись в файле?\n'\
    '3. Вывести весь файл?\n' \
    '4. Удалить запись из файла?\n' \
    '5. Выйти из программы.\n'

a = None
while a != '5':
    a = input(text_zapros)
    if a == '1':
        result = add_file(os.getcwd)
        print(result)
    if a == '2':
        to_searh = input('Введите строку для поиска ')
        result = find_el(os.getcwd(), to_searh)
        print(result)
    if a == '3':
        result = show_all(os.getcwd())
        print(result)
    if a == '4':
        to_searh = input('Введите строку для удаления ')
        result = del_line(os.getcwd(), to_searh)
        print(result)
print()


