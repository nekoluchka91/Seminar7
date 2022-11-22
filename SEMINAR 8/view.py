def view_data(self, id='', name='', department='', phone=''): 

    for i in id:
        result = f'{id[i]} {name[i]} {department[i]} {phone[i]}'
        print(result)
