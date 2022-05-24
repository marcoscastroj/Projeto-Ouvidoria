from funcoes import *

option = -1
while True:
    print('''ABC University Ombudsman:
    1) List all manifestations
    2) List all suggestions
    3) List all questions
    4) List all compliments
    5) Submit a manifestation (create a new one)
    6) Search protocol by number (ID)
    7) Leave''')
    while True:
        try:
            option = int(input('Enter an option: '))
            if option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 7:
                option = int(input('Digite uma opção valida: '))
        except(ValueError, TypeError):
            print('Please enter a valid option! ')
            continue
        else:
            print(f'Introducing the option: {option}')
            break

    # OPTION TO END THE SYSTEM
    if option == 7:
        print('End of Program!')
        break

    # OPTION TO CREATE A MANIFESTATION
    elif option == 5:
        createManifestation()

    # OPTION TO LIST THE MANIFESTATIONS
    elif option == 1:
        listDemonstrations()

    # OPTION TO LIST THE SUGGESTIONS
    elif option == 2:
        listSuggestions()

    # OPTION TO LIST THE COMPLAINTS
    elif option == 3:
        listComplaints()

    # OPTION TO LIST THE COMPLIMENTS
    elif option == 4:
        listPraise()

    # OPTION TO SEARCH BY PROTOCOL
    elif option == 6:
        searchProtocol()
