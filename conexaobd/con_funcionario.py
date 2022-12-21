from conexaobd.conexao_db import conexao_bd


class ConexaoFuncionario:

    # Função para Cadastrar um Funcionario no Banco de Dados. #
    @staticmethod
    def cadastrar_funcionario_db(funcionario):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "INSERT INTO `funcionario` (`cpf`, `nome`, `funcao`, `salario`, `telefone`) VALUES (%s, %s, %s, %s, %s)"
                c.execute(sql, (funcionario.cpf, funcionario.nome, funcionario.funcao, funcionario.salario, funcionario.telefone))
            connection.commit()
        except Exception as erro:
            print('Erro no Cadastro do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Pesquisar um Funcionário pelo CPF no Banco de Dados. #
    @staticmethod
    def pesquisar_funcionario(cpf):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `FN`.*, `FC`.`nome` AS 'nome_funcao' FROM `funcionario` AS `FN` INNER JOIN `funcao` AS `FC` ON `FN`.`funcao` = `FC`.`id` WHERE `cpf` = %s"
                c.execute(sql, cpf)
                return c.fetchone()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Pesquisar o CPF de todos os Funcionários no Banco de Dados. #
    @staticmethod
    def buscar_cpf_todos_funcionarios():
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `cpf` FROM `funcionario`"
                c.execute(sql)
                return c.fetchall()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Retorna o Id de um Funcionario no Banco de Dados. #
    @staticmethod
    def id_funcionario(cpf):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `id` FROM `funcionario` WHERE `cpf` = %s"
                c.execute(sql, cpf)
                return c.fetchone()['id']
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Editar um Funcionário no Banco de Dados. #
    @staticmethod
    def editar_funcionario(id, func):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "UPDATE `funcionario` SET `cpf` = %s, `nome` = %s, `funcao` = %s, `salario` = %s, `telefone` = %s WHERE `id` = %s"
                c.execute(sql, (func.cpf, func.nome, func.funcao, func.salario, func.telefone, id))
            connection.commit()
        except Exception as erro:
            print('Erro ao Editar Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Deletar um Funcionário do Banco de Dados. #
    @staticmethod
    def deletar_funcionario(cpf):
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "DELETE FROM `funcionario` WHERE `cpf` = %s"
                c.execute(sql, cpf)
            connection.commit()
        except Exception as erro:
            print('Erro ao Deletar Banco de Dados:', erro)
        finally:
            connection.close()

    # Função para Pesquisar todas as Funcões no Banco de Dados. #
    @staticmethod
    def buscar_funcoes_todos_funcionarios():
        connection = conexao_bd()
        try:
            with connection.cursor() as c:
                sql = "SELECT `funcao` FROM `funcionario`"
                c.execute(sql)
                return c.fetchall()
        except Exception as erro:
            print('Erro na Busca do Banco de Dados:', erro)
        finally:
            connection.close()
