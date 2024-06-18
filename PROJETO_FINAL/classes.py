from abc import ABC, abstractmethod

class Disciplina:
    def __init__(self, nome_disciplina, notas):
        self.nome = nome_disciplina
        self.notas = notas
    
    def media(self):
        self.media_aluno = sum(self.notas)/len(self.notas)
        return self.media_aluno

    def situacao(self):

        if self.media_aluno >=6:
            return 'Aprovado'
        
        elif self.media_aluno < 6 and self.media_aluno >=4:
            return 'Recuperação'
        
        else:
            return 'Reprovado'

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    
    def apresentar(self):
        print(f'Olá, meu nome é: {self.nome}')

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):

        super().__init__(nome, cpf)
        self.matricula = matricula
        self.disciplinas = []
    
    def boletim(self):

        print('-'*30)
        print('Boletim:')
        if len(self.disciplinas) == 0:
            print(f'O aluno {self.nome} ainda não cursou nenhuma disciplina!')
        else:
            for n, disciplina in enumerate(self.disciplinas):
                print(f'{n+1} - {disciplina.nome:<20}{disciplina.media():>5} -> {disciplina.situacao():<10}')

        print('-'*30)

    def cr(self):

        notas = []

        for disciplina in self.disciplinas:
            nota = disciplina.media()
            notas.append(nota)
        
        cr = sum(notas)/len(notas)

        print(f'Cr do aluno: {cr}')

    def inserir_disciplina(self):

        lista_de_notas = []

        disciplina_a_matricular = input('Digite o nome da disciplina: ')

        while True:
            nota_obtida = float(input('Digite a nota do aluno: '))
            lista_de_notas.append(nota_obtida)
            escolha = input('Deseja continuar: [S]/[N]').upper()
            if escolha == 'N':
                break

        disciplina = Disciplina(disciplina_a_matricular, lista_de_notas)
        self.disciplinas.append(disciplina)

    def apagar_disciplina(self, posicao):
        self.disciplinas.pop(posicao)

"""aluno = Aluno('Marcos', 123456789, 20192)
aluno.inserir_disciplina()
aluno.cr()
    """