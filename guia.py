from funcionario import Funcionario

class Guia(Funcionario):
    def __init__(self, nome, idioma):
        super().__init__(nome, "Guia")
        self.__idioma = idioma

    def descrever_funcao(self):
        return f"{self._nome} é um guia que fala {self.__idioma}."
