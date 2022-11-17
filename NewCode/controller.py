import model
import view
import userinterface

def button_click():
    push_button = userinterface.menu()
    if push_button == 1:
        view.view_data(*model.init())
        button_click()
    elif push_button == 2:
        view.view_data(*model.create_phonebook()) 
    elif push_button == 3:
        view.view_data(model.download_phonebook())
    elif push_button == 4:
        print('До свидания!')
    else: 
        print ('Выберите действие:')
        button_click()