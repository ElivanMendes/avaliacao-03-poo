class Validacoes:

    # Função para Verificar se a Opção Digitada foi um Valor Inteiro. #
    @staticmethod
    def verificar_opc_digitada(opc):
        try:
            opc = int(opc)
            return opc
        except ValueError:
            return -1

    # Função que Ler e Verifica o Tamanho do Código. #
    @staticmethod
    def ler_cod_funcao():
        while True:
            cod = input('\nCódigo: ')
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
