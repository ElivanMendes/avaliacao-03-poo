import pymysql


# Conexão com o Banco de Dados. #
def conexao_bd():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='developer',
                                     password='1234567',
                                     database='circuito',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except Exception as erro:
        print('Erro na Conexão:', erro)
