import info_person
import UI
import generator

def start():
    push_button = generator.menu()
    if push_button == 1:
        UI.show(*info_person.create_data())
        start()
    elif push_button == 2:
        UI.show(*info_person.get_data()) 
    elif push_button == 3:
        UI.show(*info_person.change_data())
    elif push_button == 4:
        info_person.save_data()
    elif push_button == 5:
        print('До свидания!')
    else: 
        print ('Выберите действие:')
        start()