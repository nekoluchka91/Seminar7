def menu():
    menu_list = {
            1: 'Создать телефонный справочник',
            2: 'Загрузить справочник из файла',
            3: 'Изменить данные справочника',
            4: 'Сохранить справочник в файл',
            5: 'Выход'}
    a=(int(input(f'{menu_list} Выберите нужное действие со справочником: ')))
    return a

