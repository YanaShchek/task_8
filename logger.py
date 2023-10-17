from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nIn what format should the data be recorded\n'
                    f'1 variant:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 variant:\n'
                    f'{name}\n;{surname};{phone};{adress}\n\n'
                    f'Your choice: '))
                    
    if var == 1:
        with open('data_first_variant.csv','a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n')
    else:
        with open('data_second_variant.csv','a', encoding='utf-8') as file:
            file.write(f'{name}\n;{surname};{phone};{adress}\n\n')

def print_data():
    print('1 file')
    with open("data_first_variant.csv", 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            print(i, end='')

    print('2 file')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end='')

from data_create import input_user_data

def edit_data():
    var = int(input(f'\nIn which file to change the data\n'
                    f'1 or 2 file?'))
    if var == 1:
        with open('data_first_variant.csv','r', encoding='utf-8') as file:
            data = file.read()
            index_edit_data = int(input('Enter the line number to edit: '))
            data_lines = data.split('\n')
            edit_data_lines = data_lines[index_edit_data]
            


            
    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        

    with open(filename, «r», encoding=’utf-8′) as data:
        tel_book = data.read()
        print(tel_book)
        print(«»)
        index_delete_data = int(input(«Введите номер строки для редактирования: «)) — 1
        tel_book_lines = tel_book.split(«\n»)
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(» | «)
        fio = input(«Введите ФИО: «)
        phone = input(«Введите номер телефона: «)
        num = elements[0]
if len(fio) == 0:
fio = elements[1]
if len(phone) == 0:
phone = elements[2]
edited_line = f»{num} | {fio} | {phone}»
tel_book_lines[index_delete_data] = edited_line
print(f»Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n»)
with open(filename, «w», encoding=’utf-8′) as f:
f.write(«\n».join(tel_book_lines))