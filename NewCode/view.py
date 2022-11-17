def view_data(*data):
    id, name, lastname, phone = data
    result = ''
    print('id name_user lastname_user phone_number')
    for i in id:
        result = str(id[i])+' '+str(name[i])+' '+str(lastname[i])+\
            ' '+str(phone[i])
        print(result)
   