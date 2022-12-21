from conexaobd.con_funcao import ConexaoFuncao
from conexaobd.con_funcionario import ConexaoFuncionario


class Validacoes:

    # Função para Verificar se a Opção Digitada foi um Valor Inteiro. #
    @staticmethod
    def verificar_opc_digitada(opc):
        try:
            opc = int(opc)
            return opc
        except ValueError:
            return -1

    # Função que Verifica se o Código Informado já Existe no Banco de Dados. #
    @staticmethod
    def verificar_cod(codigo):
        lista = ConexaoFuncao.buscar_cod_todas_funcao()
        for i in lista:
            if i['cod'] == codigo:
                return True
        return False

    # Função que Ler e Verifica se o Código Cadastrado já Existe no Banco de Dados. #
    @staticmethod
    def ler_cod_funcao():
        while True:
            cod = input('\nCódigo: ')
            if len(cod) > 5:
                print('\nInforme um Código Menor que 5 Caracteres.')
                continue
            if Validacoes.verificar_cod(cod):
                print('\nCódigo já Cadastrado. Informe um Novo Código.')
                continue
            return cod

    # Função que Ler e Verifica o Tamanho do Código Buscado. #
    @staticmethod
    def ler_cod_buscado(msg):
        while True:
            cod = input(msg)
            if len(cod) > 5:
                print('\nInforme um Código Menor que 5 Caracteres.')
                continue
            return cod

    # Função que Ler e Verifica o Tamanho do Nome. #
    @staticmethod
    def ler_nome(nome):
        while True:
            nome = input(nome)
            if len(nome) > 50:
                print('\nInforme um Nome Menor que 50 Caracteres.\n')
                continue
            return nome

    # Função que Ler e Verificar um CPF. #
    @staticmethod
    def ler_cpf():
        while True:
            cpf = input('CPF: ')
            if len(cpf) != 11:
                print('\nInforme um CPF com 11 Digitos. Ex.: 64475656400\n')
                continue
            try:
                cpf = int(cpf)
                if Validacoes.verificar_cpf(str(cpf)):
                    print('\nCPF já Cadastrado. Informe um CPF Diferente.\n')
                    continue
                return cpf
            except ValueError:
                print('\nInforme Somente Números. Ex.: 64475656400\n')
                continue

    # Função que Ler e Verificar um CPF Buscado. #
    @staticmethod
    def ler_cpf_buscado(msg):
        while True:
            cpf = input(msg)
            if len(cpf) != 11:
                print('\nInforme um CPF com 11 Digitos. Ex.: 64475656400')
                continue
            try:
                cpf = int(cpf)
                return cpf
            except ValueError:
                print('\nInforme Somente Números. Ex.: 64475656400')
                continue

    # Função que Ler e Verifica um Telefone. #
    @staticmethod
    def ler_telefone():
        while True:
            telefone = input('Telefone: ')
            if len(telefone) != 11:
                print('\nInforme um Telefone com 11 Digitos. Ex.: 99981123456\n')
                continue
            try:
                telefone = int(telefone)
                return telefone
            except ValueError:
                print('\nInforme Somente Números. Ex.: 99981123456\n')
                continue

    # Função que Ler e Verifica um Salário. #
    @staticmethod
    def ler_salario():
        while True:
            salario = input('Salario: ')
            try:
                salario = float(salario)
                if salario < 0:
                    print('\nInforme um Salário Positivo.\n')
                    continue
                else:
                    return salario
            except ValueError:
                print('\nInforme um Salário Valido.\n')
                continue

    # Função que Ler e Verifica uma Função. #
    @staticmethod
    def ler_funcao():
        while True:
            cod_funcao = input('Código da Função: ')
            if len(cod_funcao) > 5:
                print('\nInforme um Código Menor que 5 Caracteres.\n')
                continue
            if not Validacoes.verificar_cod(cod_funcao):
                print('\nInforme o Código de uma Função Existente.\n')
                continue
            return ConexaoFuncao.id_funcao(cod_funcao)

    # Função que Verifica se o Código Informado já Existe no Banco de Dados. #
    @staticmethod
    def verificar_cpf(cpf):
        lista = ConexaoFuncionario.buscar_cpf_todos_funcionarios()
        for i in lista:
            if i['cpf'] == cpf:
                return True
        return False
