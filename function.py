import mysql.connector

connection = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='1234',
    database='ouvidoria'
)


class Manifestation:
    name = ''
    type = 0
    description = ''


manifestationList = []
typesList = ['Complaint', 'Suggestion', 'Praise']


def createManifestation():
    print('Enter the new manifestation:')
    name = input('Type your name: ')
    amountTypes = len(typesList)
    for i in range(amountTypes):
        print(i + 1, ')', typesList[i])
    while True:
        try:
            type = int(input('Enter the type number: '))
            if type != 1 and type != 2 and type != 3:
                type = int(input('Enter a valid number for the type: '))
        except(ValueError, TypeError):
            print('Please enter a valid option! ')
            continue
        else:
            type = typesList[type - 1]
            print('Registered type')
            break

    description = input('Enter Description: ')

    newManifestation = Manifestation()
    newManifestation.name = name
    newManifestation.type = type
    newManifestation.description = description

    manifestationList.append(newManifestation)

    cursor = connection.cursor()

    command = f'''INSERT INTO manifestacao (nome, tipo, descricao) VALUES ("{name}","{type}","{description}")'''
    cursor.execute(command)
    connection.commit()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if description == manifestacao[3]:
            print(f'Your protocol is: {manifestacao[0]}')


def listDemonstrations():
    print('List of demonstrations:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()

    for manifestacao in manifestacoes:
        print(f'Name: {manifestacao[1]}')
        print(f'type: {manifestacao[2]}')
        print(f'description: {manifestacao[3]}')
        print(f'protocol: {manifestacao[0]}')
        print()


def listSuggestions():
    print('Suggestions list:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Suggestion':
            print(f'Name {manifestacao[1]}')
            print(f'Description: {manifestacao[3]}')
            print(f'protocol: {manifestacao[0]}')
            print()


def listComplaints():
    print('List of Complaints:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Complaint':
            print(f'Name {manifestacao[1]}')
            print(f'Description: {manifestacao[3]}')
            print(f'protocol: {manifestacao[0]}')
            print()


def listPraise():
    print('Praise list:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Praise':
            print(f'Name {manifestacao[1]}')
            print(f'Description: {manifestacao[3]}')
            print(f'protocol: {manifestacao[0]}')
            print()


def searchProtocol():
    while True:
        try:
            pesquisa_protocolo = int(input('Enter your protocol: '))
        except(ValueError, TypeError):
            print('Enter a valid protocol! ')
            continue
        else:
            print('Here is the protocol: ')
            print()
            cursor = connection.cursor()
            consulta_sql = f'SELECT * FROM manifestacao where id = {pesquisa_protocolo} '
            cursor.execute(consulta_sql)
            manifestacoes = cursor.fetchall()
            for manifestacao in manifestacoes:
                print(f'Name: {manifestacao[1]}')
                print(f'Type: {manifestacao[2]}')
                print(f'Description: {manifestacao[3]}')
                print(f'Protocol: {manifestacao[0]}')
                print()
                break
            break
