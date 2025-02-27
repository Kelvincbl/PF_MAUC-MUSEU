from funcionario import Funcionario

class Curador(Funcionario):
    def __init__(self, nome, especialidade):
        super().__init__(nome, "Curador")
        self.__especialidade = especialidade

    def descrever_funcao(self):
        return f"{self._nome} é um curador especializado em {self.__especialidade}."
