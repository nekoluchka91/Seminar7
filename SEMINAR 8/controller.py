import model
import view
import userinterface

def button_click():
    push_button = userinterface.menu()
    if push_button == 1:
        view.view_data(model.download_phonebook())
        button_click()
    elif push_button == 2:
        view.view_data(model.add_info()) 
    elif push_button == 3:
        view.view_data(model.deleted_info())
    elif push_button == 4:
        view.view_data(*model.record_info())
    elif push_button == 5:
        print('До свидания!')
    else: 
        print ('Выберите действие:')
        button_click()