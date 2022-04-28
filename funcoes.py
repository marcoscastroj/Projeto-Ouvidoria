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
        print(i+1, ')', lista_tipos[i])
    while True:
        try:
            type = int(input('Digite o numero do tipo: '))
            if type != 1 and type != 2 and type != 3:
                type = int(input('Digite um numero valido referente ao tipo: '))
        except(ValueError, TypeError):
            print('Digite uma opção valida! ')
            continue
        else:
            type = lista_tipos[type-1]
            print('Tipo registrado')
            break
    descricao = input('Digite a Descrição: ')
    protocolo = len(lista_manifestacoes) + 1
    print(f'O seu protocolo é {protocolo}')

    nova_manifestacao = Manifestacao()
    nova_manifestacao.nome = name
    nova_manifestacao.tipo = type
    nova_manifestacao.descricao = descricao
    nova_manifestacao.protocolo = protocolo

    lista_manifestacoes.append(nova_manifestacao)

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
    for manifestacao in lista_manifestacoes:
        print(f'Nome: {manifestacao.nome}')
        print(f'tipo: {manifestacao.tipo}')
        print(f'descrição: {manifestacao.descricao}')
        print(f'protocolo: {manifestacao.protocolo}')
        print()
    if lista_manifestacoes == []:
        print('NÃO EXISTEM MANIFESTAÇÕES')


def opcao_2():
    print('Lista de Sugestões:')
    print()
    for manifestacao in lista_manifestacoes:
        if manifestacao.tipo == 'Sugestao':
            print(f'Nome: {manifestacao.nome}')
            print(f'descrição: {manifestacao.descricao}')
            print(f'protocolo: {manifestacao.protocolo}')
            print()
    if lista_sugestoes == []:
        print('Não Existem Sugestões')


def opcao_3():
    print('Lista de Reclamações:')
    print()
    for manifestacao in lista_manifestacoes:
        if manifestacao.tipo == 'Reclamação':
            print(f'Nome: {manifestacao.nome}')
            print(f'descrição: {manifestacao.descricao}')
            print(f'protocolo: {manifestacao.protocolo}')
            print()
    if lista_reclamacoes == []:
        print('Não Existem Reclamações!')


def opcao_4():
    print('Lista de elogios:')
    print()
    for manifestacao in lista_manifestacoes:
        if manifestacao.tipo == 'Elogio':
            print(f'Nome: {manifestacao.nome}')
            print(f'descrição: {manifestacao.descricao}')
            print(f'protocolo: {manifestacao.protocolo}')
            print()
    if lista_elogio == []:
        print('Não existem Elogios!')


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
            for manifestacao in lista_manifestacoes:
                if manifestacao.protocolo == pesquisa_protocolo:
                    print(f'Nome: {manifestacao.nome}')
                    print(f'tipo: {manifestacao.tipo}')
                    print(f'descrição: {manifestacao.descricao}')
                    print(f'protocolo: {manifestacao.protocolo}')
                    print()
                    break
                else:
                    print('Protocolo nao existe ou nao é valido!')
                    print()
                    break
            break

