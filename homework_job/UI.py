def show (key, user, bd, work, phone1, phone2):
    result = ''
    print('id name birthday job firstphone secondphone')
    for i in key:
        result = str(key[i])+' '+(user[i])+' '+str(bd[i])+\
            ' '+str(work[i])+' '+str(phone1[i])+' '+str(phone2[i])
        print(result)

