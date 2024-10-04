import mysql.connector


conexao = mysql.connector.connect(host='localhost', user='root',password='123456', database='daat0014')
cursor = conexao.cursor()

comandosql = 'select firma from daat0014.cab'
cursor.execute(comandosql)

resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()