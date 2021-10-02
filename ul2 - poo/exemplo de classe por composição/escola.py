
#Relacionamento entre classes - Composição

from departamento import Departamento

#Exemplo(s) de associação
class Escola:
    def __init__(self, nome, tipo, nomeDepartamento, estudante):
        self.__nome = nome
        self.__tipo = tipo
        self.__departamento = Departamento(nomeDepartamento)
        self.__estudante = estudante

    def get_nome(self):
        return self.__nome

    def get_tipo(self):
        return self.__tipo

    def get_departamento(self):
        return self.__departamento

    def get_estudante(self):
        return self.__estudante
