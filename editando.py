import mysql.connector


conexao = mysql.connector.connect(host='localhost', user='root',password='123456', database='daat0014')
cursor = conexao.cursor()

comandosql = 'update daat0014.cab set firma="ZZZZZZZZZZ" where firma="OUTRA FIRMA"'
cursor.execute(comandosql)
conexao.commit();

print("Gravação OK")


cursor.close()
conexao.close()