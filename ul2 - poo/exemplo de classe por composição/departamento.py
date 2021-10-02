#Exemplo de classe por composição

class Departamento:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
