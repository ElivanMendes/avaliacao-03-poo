class Funcao:
    def __int__(self, codigo, funcao):
        self.__codigo = codigo
        self.__funcao = funcao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao
