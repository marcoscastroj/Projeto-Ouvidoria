import mysql.connector

connection = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='1234',
    database='ouvidoria'
)


class Manifestacao:
    nome = ''
    tipo = 0
    descricao = ''
    protocolo = 0


lista_manifestacoes = []
lista_tipos = ['Reclamação', 'Sugestao', 'Elogio']
lista_sugestoes = []
lista_reclamacoes = []
lista_elogio = []


def opcao_5():
    print('Digite a nova manifestação:')
    name = input('Digite seu nome: ')
    quantidade_tipos = len(lista_tipos)
    for i in range(quantidade_tipos):
        print(i + 1, ')', lista_tipos[i])
    while True:
        try:
            type = int(input('Digite o numero do tipo: '))
            if type != 1 and type != 2 and type != 3:
                type = int(input('Digite um numero valido referente ao tipo: '))
        except(ValueError, TypeError):
            print('Digite uma opção valida! ')
            continue
        else:
            type = lista_tipos[type - 1]
            print('Tipo registrado')
            break

    descricao = input('Digite a Descrição: ')

    nova_manifestacao = Manifestacao()
    nova_manifestacao.nome = name
    nova_manifestacao.tipo = type
    nova_manifestacao.descricao = descricao

    lista_manifestacoes.append(nova_manifestacao)

    cursor = connection.cursor()

    command = f'''INSERT INTO manifestacao (nome, tipo, descricao) VALUES ("{name}","{type}","{descricao}")'''
    cursor.execute(command)
    connection.commit()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if descricao == manifestacao[3]:
            print(f'seu protocolo é {manifestacao[0]}')



    for manifestacao in lista_manifestacoes:
        if manifestacao.tipo == 'Reclamação':
            lista_reclamacoes.append(nova_manifestacao)
        elif manifestacao.tipo == 'Elogio':
            lista_elogio.append(nova_manifestacao)
        elif manifestacao.tipo == 'Sugestao':
            lista_sugestoes.append(nova_manifestacao)


def opcao_1():
    print('Lista de manifestações:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()

    for manifestacao in manifestacoes:
        print(f'Nome: {manifestacao[1]}')
        print(f'tipo: {manifestacao[2]}')
        print(f'descrição: {manifestacao[3]}')
        print(f'protocolo: {manifestacao[0]}')
        print()


def opcao_2():
    print('Lista de Sugestões:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Sugestao':
            print(f'Nome: {manifestacao[1]}')
            print(f'descrição: {manifestacao[3]}')
            print(f'protocolo: {manifestacao[0]}')
            print()


def opcao_3():
    print('Lista de Reclamações:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Reclamação':
            print(f'Nome: {manifestacao[1]}')
            print(f'descrição: {manifestacao[3]}')
            print(f'protocolo: {manifestacao[0]}')
            print()


def opcao_4():
    print('Lista de elogios:')
    print()
    cursor = connection.cursor()
    consulta_sql = 'SELECT * FROM manifestacao'
    cursor.execute(consulta_sql)
    manifestacoes = cursor.fetchall()
    for manifestacao in manifestacoes:
        if manifestacao[2] == 'Elogio':
            print(f'Nome: {manifestacao[1]}')
            print(f'descrição: {manifestacao[3]}')
            print(f'protocolo: {manifestacao[0]}')
            print()


def opcao_6():
    while True:
        try:
            pesquisa_protocolo = int(input('Digite o seu protocolo: '))
        except(ValueError, TypeError):
            print('Digite um protocolo valido! ')
            continue
        else:
            print('Aqui esta o protocolo: ')
            print()
            cursor = connection.cursor()
            consulta_sql = f'SELECT * FROM manifestacao where {pesquisa_protocolo} '
            cursor.execute(consulta_sql)
            manifestacoes = cursor.fetchall()
            for manifestacao in manifestacoes:
                print(f'Nome: {manifestacao[1]}')
                print(f'tipo: {manifestacao[2]}')
                print(f'descrição: {manifestacao[3]}')
                print(f'protocolo: {manifestacao[0]}')
                print()
                break
            break
