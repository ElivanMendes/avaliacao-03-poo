from classes.validacoes import Validacoes as vl
from classes.funcao import Funcao
from classes.funcionario import Funcionario
from conexaobd.con_funcao import ConexaoFuncao
from conexaobd.con_funcionario import ConexaoFuncionario


# Função que Criar uma Instância de Função. E Cadastrar no Banco de Dados. #
def cadastrar_funcao():
    codigo = vl.ler_cod_funcao('\nCódigo: ')
    nome = vl.ler_nome('Nome: ')
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
        nome = vl.ler_nome('Novo Nome: ')
        ConexaoFuncao.editar_funcao(Funcao(codigo, nome))
        print('\nFunção Editada com Sucesso.')
    else:
        print('Código da Função Não Encontrada!')


# Função que Deleta uma Função no Banco de Dados. #
def deletar_funcao():
    codigo = vl.ler_cod_buscado('\nInforme o Código da Função a Deletar: ')
    if vl.verificar_cod(codigo):
        try:
            vl.lancar_excecao(ConexaoFuncao.id_funcao(codigo))
        except Exception as erro:
            print(erro)
            return
        ConexaoFuncao.deletar_funcao(codigo)
        print('\nFunção Deletada com Sucesso.')
    else:
        print('\nCódigo da Função Não Encontrada!')


# Função que Criar uma Instância de Funcionario. E Cadastrar no Banco de Dados. #
def cadastrar_funcionario():
    nome = vl.ler_nome('\nNome: ')
    cpf = vl.ler_cpf()
    funcao = vl.ler_funcao()
    salario = vl.ler_salario()
    telefone = vl.ler_telefone()
    ConexaoFuncionario.cadastrar_funcionario_db(Funcionario(nome, cpf, funcao, salario, telefone))
    print('\nCadastro Realizado com Sucesso.')


# Função para Imprimir um Funcionário. #
def imprimir_funcionario(f):
    print('\n==================================')
    print('Nome: {}'.format(f['nome']))
    print('CPF: {}.{}.{}-{}'.format(f['cpf'][:3], f['cpf'][3:6], f['cpf'][6:9], f['cpf'][9:]))
    print('Função: {}'.format(f['nome_funcao']))
    print('Salário: R$ {:.2f}'.format(f['salario']).replace('.', ','))
    print('Telefone: ({}){}-{}'.format(f['telefone'][:2], f['telefone'][2:7], f['telefone'][7:]))
    print('==================================')


# Função para Pesquisar um Funcionário no Banco de Dados. #
def pesquisar_funcionario():
    funcionario = ConexaoFuncionario.pesquisar_funcionario(vl.ler_cpf_buscado('\nInforme o CPF Buscado: '))
    if funcionario:
        imprimir_funcionario(funcionario)
    else:
        print('\nFuncionário Não Encontrado!')


# Função que Editar um Funcionário no Banco de Dados. #
def editar_funcionario():
    cpf = vl.ler_cpf_buscado('\nInforme o CPF do Funcionário a Editar: ')
    print()
    if vl.verificar_cpf(str(cpf)):
        nome = vl.ler_nome('Novo Nome: ')
        funcao = vl.ler_funcao()
        salario = vl.ler_salario()
        telefone = vl.ler_telefone()
        ConexaoFuncionario.editar_funcionario(Funcionario(nome, cpf, funcao, salario, telefone))
        print('\nFuncionário Editado com Sucesso.')
    else:
        print('CPF Não Encontrada!')


# Função que Deleta um Funcionário no Banco de Dados. #
def deletar_funcionario():
    cpf = vl.ler_cpf_buscado('\nInforme o CPF do Funcionário a Deletar: ')
    if vl.verificar_cpf(str(cpf)):
        ConexaoFuncionario.deletar_funcionario(cpf)
        print('\nFuncionário Deletado com Sucesso.')
    else:
        print('\nCPF Não Encontrada!')


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
            if ConexaoFuncao.buscar_cod_todas_funcao():
                cadastrar_funcionario()
            else:
                print('\nNão há Funções Cadastradas! Cadastre uma Função para Cadastrar um Funcionario.')
        elif opc == 2:
            if ConexaoFuncionario.buscar_cpf_todos_funcionarios():
                pesquisar_funcionario()
            else:
                print('\nNão há Funcionários Cadastradas!')
        elif opc == 3:
            if ConexaoFuncionario.buscar_cpf_todos_funcionarios():
                editar_funcionario()
            else:
                print('\nNão há Funcionários Cadastradas!')
        elif opc == 4:
            if ConexaoFuncionario.buscar_cpf_todos_funcionarios():
                deletar_funcionario()
            else:
                print('\nNão há Funcionários Cadastradas!')
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
