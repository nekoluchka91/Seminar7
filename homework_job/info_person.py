def create_data():
    import random
    from datetime import date
    global id
    global name
    global birthday
    global job
    global first_phone
    global second_phone
    id = []
    name = []
    birthday = []
    job = []
    first_phone = []
    second_phone = []

    n = int(input('Введите размер списка, количество строк'))
    for i in range(n*1):
        id.append(i)
        name.append('user'+str(i))
        birthday.append(date.today().replace(day=random.randint(
            1, 30), month=random.randint(1, 12), 
            year=random.randint(1970, 2002)))
        job.append(random.randint(1, 10))
        first_phone.append(random.randint(100000, 999999))
        second_phone.append(random.randint(100000, 999999))
    return(id, name, birthday, job, first_phone, second_phone)

    
def save_data():
    global id
    global name
    global birthday
    global job
    global first_phone
    global second_phone

    with open('result_download.csv', 'w') as file:
        for i in id:
            file.writelines(str(id[i])+''+name[i]+''+str(birthday[i])+ \
            ''+str(job[i])+''+str(first_phone[i])+''+str(second_phone[i]))


def get_data():
    global id
    global name
    global birthday
    global job
    global first_phone
    global second_phone
    id = []
    name = []
    birthday = []
    job = []
    first_phone = []
    second_phone = []
    data = open('result_upload.csv', 'r')
    for line in data:
        items = []
        items = line.split()
        id.append(int(items[0]))
        name.append(items[1])
        birthday.append(items[2])
        job.append(items[3])
        first_phone.append(items[4])
        second_phone.append(items[5])
    data.close()
    return(id, name, birthday, job, first_phone, second_phone)