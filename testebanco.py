import mysql.connector as my
banco = my.connect(
 host='localhost',
 user='root',
 password='',
 database = 'arstotzka'
)
print(banco)
cursor = banco.cursor()
comando_SQL = 'INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)'
dados = ('Lucas','30','KLukinha@gmail.com')
cursor.execute(comando_SQL,dados)
banco.commit()



