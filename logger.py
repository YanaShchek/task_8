from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nIn what format should the data be recorded\n'
                    f'1 variant:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'1 variant:\n'
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
    with open("data_first_variant.csv", 'a', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            print(i, end='')

    print('2 file')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        for i in data:
            print(i, end='')