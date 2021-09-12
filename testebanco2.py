import mysql.connector as my
banco = my.connect(
 host='localhost',
 user='root',
 password='',
 database = 'arstotzka'
)
cursor = banco.cursor()
comando_sql = 'SELECT * FROM pessoas'
cursor.execute(comando_sql)
valores_lidos = cursor.fetchall()
print(valores_lidos)
