from funcionario import Funcionario

class Seguranca(Funcionario):
    def __init__(self, nome, turno):
        super().__init__(nome, "Segurança")
        self.__turno = turno

    def descrever_funcao(self):
        return f"{self._nome} é segurança e trabalha no turno {self.__turno}."
