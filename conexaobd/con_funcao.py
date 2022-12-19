from conexaobd.conexao_db import conexao_bd


class ConexaoFuncao:

    # Função para Cadastrar um Funcionário no Banco de Dados. #
    @staticmethod
    def cadastrar_funcao_db(funcao):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "INSERT INTO `funcao` (`cod`, `nome`) VALUES (%s, %s)"
                c.execute(sql, (funcao.codigo, funcao.nome))
            connection.commit()
        except Exception as erro:
            print('Erro no Cadastro do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Pesquisar um Funcionario pelo Código no Banco de Dados. #
    @staticmethod
    def pesquisar_funcao(cod_funcao):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT * FROM `funcao` WHERE `cod` = %s"
                c.execute(sql, cod_funcao)
                return c.fetchall()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()
