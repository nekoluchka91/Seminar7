import random
import csv

def init():
    global id # вызывает каждую перем, 
    global name # кот. сначала 0-ые, 
    global lastname # чтобы в рез-те показало значения
    global phone
    id = [] # сначала форм-ем пустое значение
    name = []
    lastname = []
    phone = []

    n = int(input('Введите количество строк в справочнике - '))
    for i in range(n):
        id.append(i)
        name.append('user_name'+str(i))
        lastname.append('user_lastname'+str(i))
        phone.append(random.randint(100, 999))

    return id, name, lastname, phone


def create_phonebook():
    global id 
    global name 
    global lastname 
    global phone

    with open('result_phonebook.csv', 'w') as file:
        for i in id:
            file.writelines(str(id[i])+' '+str(name[i])+' '+str(lastname[i])+\
                ' '+str(phone[i])+'\n')

    # return id, name, lastname, phone


def download_phonebook():
    global id 
    global name 
    global lastname 
    global phone    
    
    f = open('phonebook.csv', 'r')
    data = f.read() + ' '
    f.close()

    with open("phonebook.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
    # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
            # Вывод строк
                print(f'    {row[0]} {row[1]} {row[2]}, номер телефона пользователя {row[3]}')
            count += 1
        print(f'Всего в файле {count-1} человек.')