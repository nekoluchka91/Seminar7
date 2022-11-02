import info_person
import UI
import generator

def start():
    push_button=generator.menu()
    if push_button == 1:
        UI.show(*function.create_data())
        start()
    elif push_button == 2:
        UI.show(function.get_data())
    elif push_button == 3:
        UI.show(*function.change_data())
    elif push_button == 4:
        function.save_data()
    elif push_button == 5:
        print('До свидания!')
    else: 
        print ('Выберите действие:')
        start()