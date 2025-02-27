class Exposicao:
    def __init__(self, nome, tema):
        self.__nome = nome
        self.__tema = tema
        self.__obras = []

    def adicionar_obra(self, obra):
        self.__obras.append(obra)

    def listar_obras(self):
        return [obra.get_titulo() for obra in self.__obras]

    def get_nome(self):
        return self.__nome

    def get_tema(self):
        return self.__tema
