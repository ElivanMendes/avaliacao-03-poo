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
