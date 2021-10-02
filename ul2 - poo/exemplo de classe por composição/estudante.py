#Agregado - Exemplo de classe agregada
class Estudante:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome (self):
        return self.__nome
