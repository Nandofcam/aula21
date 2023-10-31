import pymysql.cursors

try:
    conexao = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              database='escola',
                              cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida com sucesso!')

except Exception as error:
    print(f'Erro ao conectar! {error}')

cursor = conexao.cursor()


def selectAlunos():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)
    except Exception as error:
        print(f'Erro ao listar os alunos! {error}')

def insertAluno(nome, idade, curso):
    try:
        sql = "INSERT INTO alunos (nome, idade, curso)"\
              "VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, idade, curso))
        conexao.commit()
        print('Aluno matriculado com sucesso!')
    except Exception as error:
        print(f"Erro ao cadastrar! {error}")

def updateAluno(nome, idade, curso, matricula):
    try:
        if checarMatricula(matricula):
            sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s WHERE matricula = %s"
            cursor.execute(sql, (nome, idade, curso, matricula))
            conexao.commit()
            print("Dados atualizados com sucesso!")
        else:
            print("Matrícula não encontrada!")
    except Exception as error:
        print(f"Erro ao atualizar o cadastro! {error}")

def deleteAluno(matricula):
    try:
        if checarMatricula(matricula):
            sql = "DELETE FROM alunos WHERE matricula = %s"
            cursor.execute(sql, matricula)
            conexao.commit()
            print("Dados removidos com sucesso!")
        else:
            print("Matrícula não encontrada!")
    except Exception as error:
        print(f"Erro ao remover o cadastro! {error}")

def checarMatricula(matricula):
    try:
        sql = "SELECT * FROM alunos WHERE matricula = %s"
        cursor.execute(sql, matricula)
        if len(cursor.fetchall()) == 1:
            return True
        else:
            return False
    except Exception as error:
        print(f"Erro ao consultar! {error}")