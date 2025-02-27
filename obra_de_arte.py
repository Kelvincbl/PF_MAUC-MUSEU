class ObraDeArte:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_ano(self):
        return self.__ano
