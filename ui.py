from logger import input_data, print_data

def interface():
    print('Hello! I am Chat Bot. \n'
          'What do you want?\n'
          '1 - Write down the data?\n'
          '2 - Output data?')
    command = int(input('Your choice: '))

    while command < 1 or command > 2:
        command = int(input('Mistake! Your choice: '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()