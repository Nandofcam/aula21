import aula21 as bd
def menu():
    while True:
        print('-- BEM VINDO AO MENU --')
        print('1 - Adicionar aluno')
        print('2 - Editar aluno')
        print('3 - Deletar aluno')
        print('4 - Listar todos')
        print('5 - Sair')
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            bd.insertAluno(nome, idade, curso)

        elif opcao == '2':
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            matricula = int(input('Digite a matrícula: '))
            bd.updateAluno(nome, idade, curso, matricula)

        elif opcao == '3':
            matricula = int(input('Digite a matricula do aluno: '))
            bd.deleteAluno(matricula)

        elif opcao == '4':
            bd.selectAlunos()

        elif opcao == '5':
            break

        else:
            print("Opção inválida, digite o número de uma das opções abaixo!")

menu()