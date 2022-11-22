import csv

def download_phonebook():
    global id 
    global name 
    global department
    global phone
    id = []
    name = []
    department = []
    phone = []  

    with open('phonebook.csv', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'{row[0]} сотрудник {row[1]} работает в\
                {row[2]} отделе, его номер телефона {row[3]}')
            count += 1
        print(f'Всего в файле данные о {count-1} сотрудниках.')


def add_info():
    data = []

    with open("phonebook.csv", mode="w", encoding='utf-8') as w_file:
        w_file = csv.writer(w_file, delimiter = ";")
        str_data = input('Введите через ; новые данные: ')
        row = str_data.split(';')
        data.append([row[0], row[1], row[2], row[3]])
    record_info(data)


def deleted_info():
    data = []
    
    with open('phonebook.csv', newline='', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        username = input('Введите имя работника для удаления записи о нем: ')
        for row in file_reader:
            if row[0] != username:
                data = row
                print(data)
    record_info(data)


def record_info(data):
    with open("phonebook.csv", 'w', encoding='utf-8') as w_file:
        Writer = csv.writer(w_file)
        Writer.writerow(data)
        print('Справочник обновился.')
    

