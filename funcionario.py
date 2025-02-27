class Funcionario:
    def __init__(self, nome, cargo):
        self._nome = nome
        self._cargo = cargo

    def descrever_funcao(self):
        return f"{self._nome} trabalha como {self._cargo} no museu."
