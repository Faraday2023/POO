def exibir_menu():
    print('-'*100)
    print('1 - Cadastrar Pessoa')
    print('2 - Consultar Pessoa')
    print('3 - Depósito')
    print('4 - Saque')
    print('5 - Rendimento no fim do mês')
    print('0 - Sair')
    print('-'*100)

def cadastrar_pessoa():
    nome = input('Digite o nome da pessoa: ')
    cpf = int(input('Digite o CPF da pessoa: '))
    saldo = float(input('Digite o saldo inicial em conta: '))

def listar_pessoas(lista_de_pessoas):

    for c, pessoa in enumerate(lista_de_pessoas):
        print(f'Índice: {c} - {pessoa.titular_altera} - {pessoa.cpf_altera}')

def consultar_pessoas(lista_de_pessoas):

    selecao = int(input('Deseja consultar as informações de qual pessoa: '))
    print('-'*100)

    if 0 <= selecao < len(lista_de_pessoas):
        lista_de_pessoas[selecao].imprime_saldo()

def realizar_deposito(lista_de_pessoas):

    selecao = int(input('Deseja realizar depósito em qual conta: '))
    print('-'*100)

    valor_deposito = float(input('Digite o valor do depósito: '))

    if 0 <= selecao < len(lista_de_pessoas):
        lista_de_pessoas[selecao].deposito(valor_deposito)

def realizar_saque(lista_de_pessoas):
    selecao = int(input('Deseja realizar saque em qual conta: '))
    print('-'*100)

    valor_saque = float(input('Digite o valor do saque: '))

    if 0 <= selecao < len(lista_de_pessoas):
        lista_de_pessoas[selecao].saque(valor_saque)

def rendimento_mes(lista_de_pessoas):

    selecao = int(input('Deseja conferir rendimento em qual conta: '))
    print('-'*100)

    valor_juros = float(input('Digite o valor do juros: '))

    if 0 <= selecao < len(lista_de_pessoas):
        lista_de_pessoas[selecao].rendimentos(valor_juros)
