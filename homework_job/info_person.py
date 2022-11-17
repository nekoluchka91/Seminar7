def create_data():
    import random
    from datetime import date
    global id
    global name
    global birthday
    global job
    global firstphone
    global secondphone
    id = []
    name = []
    birthday = []
    job = []
    firstphone = []
    secondphone = []

    n = int(input('Введите размер списка, количество строк - '))
    for i in range(n*1):
        id.append(i)
        name.append('user'+str(i))
        birthday.append(date.today().replace(day=random.randint(
            1, 30), month=random.randint(1, 12), 
            year=random.randint(1970, 2002)))
        job.append(random.randint(1, 10))
        firstphone.append(random.randint(100000, 999999))
        secondphone.append(random.randint(100000, 999999))
    return id, name, birthday, job, firstphone, secondphone

    
def save_data():
    global id
    global name
    global birthday
    global job
    global firstphone
    global secondphone

    with open('result_info.csv', 'w') as file:
        for i in id:
            file.writelines(str(id[i])+' '+name[i]+' '+str(birthday[i])+\
                ' '+str(job[i])+' '+str(firstphone[i])+\
                    ' '+str(secondphone[i])+'\n')


def get_data():
    global id
    global name
    global birthday
    global job
    global firstphone
    global secondphone
    id = []
    name = []
    birthday = []
    job = []
    firstphone = []
    secondphone = []
    data = open('basic_info.csv', 'r')
    for line in data:
        
        items = []
        items = line.split()

        id.append(items[0])
        name.append(items[1])
        birthday.append(items[2])
        job.append(items[3])
        firstphone.append(items[4])
        secondphone.append(items[5])
    data.close()
    return id, name, birthday, job, firstphone, secondphone


# def change_data():
    # data = open('basic_info.csv', 'w')
    # for line in data:
    #     record_id = int(input('Введите номер строки для изменения: '))
    #     box = int(input("Введите номер поля для изменения:\n"
    #                 "'1' - name\n"
    #                 "'2' - birthday\n"
    #                 "'3' - job\n"
    #                 "'4' - firstphone\n"
    #                 "'5' - secondphone\n"
    #                 "Хочу изменить поле под номером: "))

    # with open('result_afterchange.csv', 'w') as file:
    #     for line in data:
    #         record_id = int(input('Введите номер строки для изменения: '))
    #         box = int(input("Введите номер поля для изменения:\n"
    #                 "'1' - name\n"
    #                 "'2' - birthday\n"
    #                 "'3' - job\n"
    #                 "'4' - firstphone\n"
    #                 "'5' - secondphone\n"
    #                 "Хочу изменить поле под номером: "))
                
    #         file.writelines(str(id[i])+' '+name[i]+' '+str(birthday[i])+\
    #             ' '+str(job[i])+' '+str(firstphone[i])+\
    #                 ' '+str(secondphone[i])+'\n')

    # with open ('basic_info.csv', 'r') as f:
    #     old_data = f.read()

    

    # new_data = old_data.replace('Alex', 'Alexandr')

    # with open ('basic_info.csv', 'w') as f:
    #     f.write(new_data)
    
    # return id, name, birthday, job, firstphone, secondphone

    # record_id = int(input('Введите номер строки для изменения: '))
    # box = int(input("Введите номер поля для изменения:\n"
    #                 "'1' - name\n"
    #                 "'2' - birthday\n"
    #                 "'3' - job\n"
    #                 "'4' - first_phone\n"
    #                 "'5' - second_phone\n"
    #                 "Хочу изменить поле под номером: "))
    # new_record = input(f'Новая запись поля в id {record_id}: ')
    # function.change_record_id(record_id, box, new_record)
