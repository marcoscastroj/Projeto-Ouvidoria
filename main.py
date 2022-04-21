# Programa de ouvidoria da faculdade ABC
list_manifestacoes = []
tipos_manifestacoes = ['Reclamação', 'Sugestão', 'Elogio']
opcao = 0


#   Função Para Listar as manifestações
def opcao_1():
    print('Aqui está as manifestações: ')
    for manifestacao in list_manifestacoes:
        mani_quebrada = manifestacao.split('#')
        print('Protocolo: {}'.format(mani_quebrada[0]))
        print('Nome: {}'.format(mani_quebrada[1]))
        print('Tipo: {}'.format(mani_quebrada[2]))
        print('Descrição: {}'.format(mani_quebrada[3]))
        print('')


#   Função Para Listar as Sugestões
def opcao_2():
    print('Lista de Sugestões: ')
    for manifestacao in list_manifestacoes:
        mani_quebrada = manifestacao.split('#')
        if mani_quebrada[2] == 'Sugestão':
            print('Protocolo: {}'.format(mani_quebrada[0]))
            print('Nome: {}'.format(mani_quebrada[1]))
            print('Tipo: {}'.format(mani_quebrada[2]))
            print('Descrição: {}'.format(mani_quebrada[3]))
            print('')
        elif mani_quebrada[2] != 'Sugestão':
            print('')


#   Função Para Listar as Reclamações
def opcao_3():
    print('Lista de Reclamações: ')
    for manifestacao in list_manifestacoes:
        mani_quebrada = manifestacao.split('#')
        if mani_quebrada[2] == 'Reclamação':
            print('Protocolo: {}'.format(mani_quebrada[0]))
            print('Nome: {}'.format(mani_quebrada[1]))
            print('Tipo: {}'.format(mani_quebrada[2]))
            print('Descrição: {}'.format(mani_quebrada[3]))
            print('')
        elif mani_quebrada[2] != 'Reclamação':
            print('')


#   Função Para Listar os Elogios
def opcao_4():
    print('Lista de Elogios: ')
    for manifestacao in list_manifestacoes:
        mani_quebrada = manifestacao.split('#')
        if mani_quebrada[2] == 'Elogio':
            print('Protocolo: {}'.format(mani_quebrada[0]))
            print('Nome: {}'.format(mani_quebrada[1]))
            print('Tipo: {}'.format(mani_quebrada[2]))
            print('Descrição: {}'.format(mani_quebrada[3]))
            print('')
        elif mani_quebrada[2] != 'Elogio':
            print('')


#   Função Para Procurar pelo Protocolo
def opcao_6():
    for manifestacao in list_manifestacoes:
        mani_quebrada = manifestacao.split('#')
        proto = str(input('Digite o seu protocolo: '))
        if mani_quebrada[0] == proto:
            print('Protocolo: {}'.format(mani_quebrada[0]))
            print('Nome: {}'.format(mani_quebrada[1]))
            print('Tipo: {}'.format(mani_quebrada[2]))
            print('Descrição: {}'.format(mani_quebrada[3]))
            print('')
        elif proto != mani_quebrada[0]:
            print('Protocolo Inválido ou não existe!')


while True:
    # Menu
    print('''Ouvidoria Universidade ABC:
    1) Listar todas as manifestações 
    2) Listar todas as sugestões
    3) Listar todas as reclamações
    4) Listar todos os elogios
    5) Enviar uma manifestação (criar uma nova)
    6) Pesquisar protocolo por número (ID)
    7) Sair''')
    opcao = int(input('Digite uma opção: '))

    # Opção Para Finalizar o Programa
    if opcao == 7:
        print('Fim do Programa!')
        break

    # Opção Inválida
    if opcao < 1 or opcao > 7:
        print('Digite uma opção Válida!')

    # Enviar uma Manifestação
    if opcao == 5:
        print('Digite a nova manifestação:')
        nome = input('Digite Seu nome: ')
        quant_tipos = len(tipos_manifestacoes)
        for i in range(quant_tipos):
            print(i + 1, ')', tipos_manifestacoes[i])
        tipo = int(input('Digite o Tipo de Manifestação: '))
        descricao = input('Digite a Descrição: ')
        protocolo = str(len(list_manifestacoes) + 1)
        manifestacao = protocolo + '#' + nome + '#' + tipos_manifestacoes[tipo - 1] + '#' + descricao
        list_manifestacoes.append(manifestacao)

    # Listar Manifestações
    if opcao == 1:
        opcao_1()

    # Listar Todas as Sugestoes
    if opcao == 2:
        opcao_2()

    # Listar Todas as Reclamações
    if opcao == 3:
        opcao_3()

    # Listar Todos os Elogios
    if opcao == 4:
        opcao_4()

    # Consultar Protocolo
    if opcao == 6:
        opcao_6()
