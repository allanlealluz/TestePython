import mysql.connector as my
def conexao():
    banco = my.connect(
        host='localhost',
        user = 'root',
        password='',
        database= 'azaroth'
    )
    return banco
def inserir(personagens,nomehab,hab):
    banco = conexao()
    comando_sql = f'SELECT * FROM personagens Where personagens = "{personagens}" '
    cursor = banco.cursor()
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    comando_sql2 = f'INSERT INTO habs (personagem,nomehab,hab) VALUES ({dados[0][0]},"{nomehab}","{hab}")'
    cursor.execute(comando_sql2)
    banco.commit()
def inserirPersonagem(personagem):
    banco = conexao()
    comando_sql = f'INSERT INTO personagens (personagens) VALUES ("{personagem}")'
    cursor = banco.cursor()
    cursor.execute(comando_sql)
    banco.commit()
def SelecionarPersonagens():
    banco = conexao()
    comando_sql = 'SELECT * FROM personagens'
    cursor = banco.cursor()
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    return dados


