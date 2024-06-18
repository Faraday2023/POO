from funcoes import menu, menu_aluno
from classes import Aluno

# VARIÁVEIS GLOBAIS

alunos = []

while True:
    menu_principal = menu()
    escolha = input('Digite a opção desejada: ')

    if escolha == '0':
        break

    elif escolha == '1':
        nome_aluno = str(input('Digite o nome do aluno: '))
        cpf_do_aluno = int(input('Digite o CPF do aluno: '))
        matricula = int(input('Digite a matricula do aluno: '))
        aluno = Aluno(nome_aluno, cpf_do_aluno, matricula)
        alunos.append(aluno)
       
    elif escolha == '2':

        print('-= LISTAR ALUNOS =-')
        print('-'*50)
        if len(alunos) == 0:
            print('Não existem alunos cadastrados!')
        else:
            for n, aluno in enumerate(alunos):
                print(f'{n+1} - {aluno.nome}')
                print('-'*50)
        input('Pressione ENTER para continuar...')
    
    elif escolha == '3':

        print('-= CONSULTAR ALUNO =-')
        print('')
        codigo = input('Digite o código do Aluno ou ENTER para finalizar: ')

        if codigo != '':
            codigo = int(codigo)-1

        if codigo > len(alunos)-1:
            print('Código não existe!')
        else:
            aluno = alunos[codigo]
            while True:
                print(f'Aluno: {aluno.nome}')
                menu_secundario = menu_aluno()
                opcao = input('Escolha a Opção: ')

                if opcao == '1':
                    aluno.boletim()
                    input('Pressione ENTER para continuar')
                elif opcao == '2':
                    aluno.inserir_disciplina()
                    input('Pressione ENTER para continuar')
                elif opcao == '3':
                    aluno.cr()
                
                elif opcao == '4':
                    posicao = int(input('Quer apagar qual disciplina ? Digite o código dela: '))
                    aluno.apagar_disciplina(posicao-1)
                
                elif opcao == '0':
                    break

    elif escolha == '4':
        posicao_aluno = int(input('Quer apagar qual aluno ? Digite o código do aluno: '))
        alunos.pop(posicao_aluno-1)
