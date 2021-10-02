class Bebe:
    def __init__(self, nome, mae = None):
        if (mae is None):
            print ("Bebe depende de mãe, não pode instanciar")
            return

        self.__nome = nome

    def get_name (self):
        return self.__nome
