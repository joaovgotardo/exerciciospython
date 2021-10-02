from escola import Escola
from estudante import Estudante

estudante = Estudante("João")
estudante2 = Estudante("Cláudio")
estudante3 = Estudante("Fulano")
escola = Escola('Olavo', 'Estadual', 'Estudantil', estudante)

print("Escola =" + escola.get_nome())
print("Tipo =" + escola.get_tipo())
print('Nome do estudante: ' + escola.get_estudante().get_nome())

departamento = escola.get_departamento()
print("Nome do departamento=" + departamento.get_nome())

"""
Exemplos
Para classes agregadas
print('Nome do estudante: ' + escola.get_estudante().get_nome())

Para classes de composição 
departamento = escola.get_departamento()
print("Nome do departamento=" + departamento.get_nome())
"""
#type = diz o tipo do conteúdo
