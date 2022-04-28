import funcoes


opcao = -1
while True:
    print('''Ouvidoria Universidade ABC:
    1) Listar todas as manifestações 
    2) Listar todas as sugestões
    3) Listar todas as reclamações
    4) Listar todos os elogios
    5) Enviar uma manifestação (criar uma nova)
    6) Pesquisar protocolo por número (ID)
    7) Sair''')
    while True:
        try:
            opcao = int(input('Digite uma opção: '))
            if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7:
                opcao = int(input('Digite uma opção valida: '))
        except(ValueError, TypeError):
            print('Digite uma opção valida! ')
            continue
        else:
            print(f'Apresentando a opção: {opcao}')
            break

    #   OPÇÃO PARA FINALIZAR O SISTEMA
    if opcao == 7:
        print('Fim do Programa!')
        break

    #   OPÇÃO PARA CRIAR UMA MANIFESTAÇÃO
    elif opcao == 5:
        funcoes.opcao_5()

    #   OPÇÃO PARA LISTAR AS MANIFESTAÇÕES
    elif opcao == 1:
        funcoes.opcao_1()

    #   OPÇÃO PARA LISTAR AS SUGESTOES
    elif opcao == 2:
        funcoes.opcao_2()

    #   OPÇÃO PARA LISTAR AS RECLAMAÇÕES
    elif opcao == 3:
        funcoes.opcao_3()

    #   OPÇÃO PARA LISTAR OS ELOGIOS
    elif opcao == 4:
        funcoes.opcao_4()

    #   OPÇÃO PARA MOSTRAR O PROTOCOLO
    elif opcao == 6:
        funcoes.opcao_6()

