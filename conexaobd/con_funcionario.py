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
