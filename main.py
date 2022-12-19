from classes.validacoes import Validacoes as vl
from classes.funcao import Funcao
from conexaobd.con_funcao import ConexaoFuncao


# Função que Criar uma Instância de Função. #
def cadastrar_funcao():
    codigo = vl.ler_cod_funcao()
    nome = vl.ler_nome_funcao()
    return Funcao(codigo, nome)


# Função para Imprimir uma Função. #
def imprimir_funcao(funcao):
    print('\n==============================')
    for i in funcao:
        print('Código: {cod}\nFunção: {nome}'.format(cod=i['cod'], nome=i['nome']))
    print('==============================')


# Menu de Manter Funções. #
def menu_manter_funcoes():
    while True:
        print('\n========= MENU FUNÇÕES =========')
        print('1 - Cadastrar Função\n2 - Pesquisar Função\n3 - Editar Função')
        print('4 - Deletar Função\n0 - Voltar ao Menu Principal')
        print('================================')
        opc = vl.verificar_opc_digitada(input('\nInforme uma Opção: '))

        if opc == 0:
            print('\nVOLTANDO...')
            return
        elif opc == 1:
            ConexaoFuncao.cadastrar_funcao_db(cadastrar_funcao())
            print('\nCadastro Realizado com Sucesso.')
        elif opc == 2:
            funcao = ConexaoFuncao.pesquisar_funcao(vl.ler_cod_funcao())

            if funcao:
                imprimir_funcao(funcao)
            else:
                print('\nFunção Não Encontrada!')

        elif opc == 3:
            pass
        elif opc == 4:
            pass
        else:
            print('\nOpção Invalida!')


# Menu de Manter Funcionários. #
def menu_manter_funcionario():
    while True:
        print('\n======= MENU FUNCIONÁRIOS ======')
        print('1 - Cadastrar Funcionário\n2 - Pesquisar Funcionário\n3 - Editar Funcionário')
        print('4 - Deletar Funcionário\n0 - Voltar ao Menu Principal')
        print('================================')
        opc = vl.verificar_opc_digitada(input('\nInforme uma Opção: '))

        if opc == 0:
            print('\nVOLTANDO...')
            return
        elif opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        else:
            print('\nOpção Invalida!')


# Menu Principal. #
def menu_principal():
    while True:
        print('\n======== MENU PRINCIPAL ========')
        print('1 - Manter Funções\n2 - Manter Funcionários\n0 - Sair')
        print('================================')
        opc = vl.verificar_opc_digitada(input('\nInforme uma Opção: '))

        if opc == 0:
            print('\nSAINDO...')
            exit()
        elif opc == 1:
            menu_manter_funcoes()
        elif opc == 2:
            menu_manter_funcionario()
        else:
            print('\nOpção Invalida!')


menu_principal()
