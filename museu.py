class Museu:
    def __init__(self, nome, localizacao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__exposicoes = []

    def adicionar_exposicao(self, exposicao):
        self.__exposicoes.append(exposicao)

    def listar_exposicoes(self):
        return [exp.get_nome() for exp in self.__exposicoes]

    def get_nome(self):
        return self.__nome

    def get_localizacao(self):
        return self.__localizacao
