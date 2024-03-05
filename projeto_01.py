# DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETO
# DESENVOLVEDOR: MARCOS PAULO P. CARNEIRO
# TURMA: 10° ENGEL

from funcionalidades import exibir_menu

class Conta():
    def __init__(self, titular, cpf, saldo=0):

        self.__titular = titular
        self.__cpf = cpf
        self.__saldo = saldo
    
    def deposito(self, valor):

        self.__saldo = self.__saldo + valor

    def saque(self, valor):

        self.__saldo = self.__saldo - valor

    def rendimentos(self, juros):

        juros = juros/100

        self.__saldo = self.__saldo + (self.__saldo*juros)

    def saldo(self):

        print(f'{self.__titular} (CPF N°: {self.__cpf}): Possui saldo em conta de R$: {self.__saldo}.')
        print('-'*100)
    
    @property # getter - Recebe o titular
    def titular_altera(self):
        return self.__titular
    
    @titular_altera.setter # setter - atualiza o titular
    def titular_altera(self, titular_novo):

        self.__titular = titular_novo

    @property # getter - Recebe o CPF
    def cpf_altera(self):
        return self.__cpf

    @cpf_altera.setter # setter - atualiza o cpf
    def cpf_altera(self, cpf_novo):

        self.__cpf = cpf_novo

# MAIN - CÓDIGO PRINCIPAL

lista_de_pessoas = []

exibir_menu()

while True:

    escolha = input('Digite a opção desejada: ')

    if escolha == '1':
        nome = input('Digite o nome da pessoa: ')
        cpf = int(input('Digite o CPF da pessoa: '))
        saldo = float(input('Digite o saldo inicial em conta: '))
        pessoa = Conta(nome, cpf, saldo)
        lista_de_pessoas.append(pessoa)
        print('-'*100)

    elif escolha == "2":

        for c, pessoa in enumerate(lista_de_pessoas):
            print(f'Índice: {c} - {pessoa.titular_altera} - {pessoa.cpf_altera}')
        
        selecao = int(input('Deseja consultar as informações de qual pessoa: '))
        print('-'*100)

        if 0 <= selecao < len(lista_de_pessoas):
            lista_de_pessoas[selecao].saldo()
    
    elif escolha == "3":

        for c, pessoa in enumerate(lista_de_pessoas):
            print(f'Índice: {c} - {pessoa.titular_altera} - {pessoa.cpf_altera}')
        
        selecao = int(input('Deseja realizar depósito em qual conta: '))
        print('-'*100)

        valor_deposito = float(input('Digite o valor do depósito: '))

        if 0 <= selecao < len(lista_de_pessoas):
            lista_de_pessoas[selecao].deposito(valor_deposito)
    
    elif escolha == "4":

        for c, pessoa in enumerate(lista_de_pessoas):
            print(f'Índice: {c} - {pessoa.titular_altera} - {pessoa.cpf_altera}')
        
        selecao = int(input('Deseja realizar saque em qual conta: '))
        print('-'*100)

        valor_saque = float(input('Digite o valor do saque: '))

        if 0 <= selecao < len(lista_de_pessoas):
            lista_de_pessoas[selecao].saque(valor_saque)
    
    elif escolha == "5":

        for c, pessoa in enumerate(lista_de_pessoas):
            print(f'Índice: {c} - {pessoa.titular_altera} - {pessoa.cpf_altera}')
        
        selecao = int(input('Deseja conferir rendimento em qual conta: '))
        print('-'*100)

        valor_juros = float(input('Digite o valor do juros: '))

        if 0 <= selecao < len(lista_de_pessoas):
            lista_de_pessoas[selecao].rendimentos(valor_juros)

    elif escolha == '0':
        break

    else:
        print('Opção inválida')
