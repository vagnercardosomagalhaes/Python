import mysql.connector


conexao = mysql.connector.connect(host='localhost', user='root',password='123456', database='daat0014')
cursor = conexao.cursor()

comandosql = 'delete from daat0014.cab where firma="ZZZZZZZZZZ"'
cursor.execute(comandosql)
conexao.commit();

print("Registro deletado")


cursor.close()
conexao.close()