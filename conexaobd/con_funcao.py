from conexaobd.conexao_db import conexao_bd


class ConexaoFuncao:

    # Função para Cadastrar uma Função no Banco de Dados. #
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

    # Função para Pesquisar uma Função pelo Código no Banco de Dados. #
    @staticmethod
    def pesquisar_funcao(cod_funcao):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT * FROM `funcao` WHERE `cod` = %s"
                c.execute(sql, cod_funcao)
                return c.fetchone()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Pesquisar o Código de todas as Funções no Banco de Dados. #
    @staticmethod
    def buscar_cod_todas_funcao():
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `cod` FROM `funcao`"
                c.execute(sql)
                return c.fetchall()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Editar uma Função no Banco de Dados. #
    @staticmethod
    def editar_funcao(funcao):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "UPDATE `funcao` SET `nome` = %s WHERE `cod` = %s"
                c.execute(sql, (funcao.nome, funcao.codigo))
            connection.commit()
        except Exception as erro:
            print('Erro ao Editar Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Deletar um Registro do Banco de Dados. #
    @staticmethod
    def deletar_funcao(codigo):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "DELETE FROM `funcao` WHERE `cod` = %s"
                c.execute(sql, codigo)
            connection.commit()
        except Exception as erro:
            print('Erro ao Deletar Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Retorna o Id de uma Função no Banco de Dados. #
    @staticmethod
    def id_funcao(cod_funcao):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `id` FROM `funcao` WHERE `cod` = %s"
                c.execute(sql, cod_funcao)
                return c.fetchone()['id']
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()
