from funcionario import Funcionario

class Administrador(Funcionario):
    def __init__(self, nome, setor):
        super().__init__(nome, "Administrador")
        self.__setor = setor

    def descrever_funcao(self):
        return f"{self._nome} é administrador do setor {self.__setor}."
