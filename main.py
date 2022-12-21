from classes.validacoes import Validacoes as vl
from classes.funcao import Funcao
from conexaobd.con_funcao import ConexaoFuncao


# Função que Criar uma Instância de Função. E Cadastrar no Banco de Dados. #
def cadastrar_funcao():
    codigo = vl.ler_cod_funcao()
    nome = vl.ler_nome()
    ConexaoFuncao.cadastrar_funcao_db(Funcao(codigo, nome))
    print('\nCadastro Realizado com Sucesso.')


# Função para Imprimir uma Função. #
def imprimir_funcao(funcao):
    print('\n==============================')
    print('Código: {cod}\nFunção: {nome}'.format(cod=funcao['cod'], nome=funcao['nome']))
    print('==============================')


# Função para Pesquisar uma Função no Banco de Dados. #
def pesquisar_funcao():
    funcao = ConexaoFuncao.pesquisar_funcao(vl.ler_cod_buscado('\nInforme o Código Buscado: '))
    if funcao:
        imprimir_funcao(funcao)
    else:
        print('\nFunção Não Encontrada!')


# Função que Editar uma Função no Banco de Dados. #
def editar_funcao():
    codigo = vl.ler_cod_buscado('\nInforme o Código da Função a Editar: ')
    print()
    if vl.verificar_cod(codigo):
        nome = vl.ler_nome()
        ConexaoFuncao.editar_funcao(Funcao(codigo, nome))
        print('\nFunção Editada com Sucesso.')
    else:
        print('Código da Função Não Encontrada!')


# Função que Deleta uma Função no Banco de Dados. #
def deletar_funcao():
    codigo = vl.ler_cod_buscado('\nInforme o Código da Função a Deletar: ')
    if vl.verificar_cod(codigo):
        ConexaoFuncao.deletar_funcao(codigo)
        print('\nFunção Deletada com Sucesso.')
    else:
        print('\nCódigo da Função Não Encontrada!')


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
            cadastrar_funcao()
        elif opc == 2:
            if ConexaoFuncao.buscar_cod_todas_funcao():
                pesquisar_funcao()
            else:
                print('\nNão há Funções Cadastradas!')
        elif opc == 3:
            if ConexaoFuncao.buscar_cod_todas_funcao():
                editar_funcao()
            else:
                print('\nNão há Funções Cadastradas!')
        elif opc == 4:
            if ConexaoFuncao.buscar_cod_todas_funcao():
                deletar_funcao()
            else:
                print('\nNão há Funções Cadastradas!')
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
