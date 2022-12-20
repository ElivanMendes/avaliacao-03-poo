from conexaobd.con_funcao import ConexaoFuncao


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
    def ler_nome_funcao():
        while True:
            nome = input('Nome: ')
            if len(nome) > 50:
                print('\nInforme um Nome Menor que 50 Caracteres.\n')
                continue
            return nome
