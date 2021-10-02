"split serve para separar dois elementos (separador)"
v_nome = 'JOÃO VITOR GOTARDO'
v_resultado = v_nome.split()

"""
Outra forma de resolver isso
if len(v_resultado) == 2:
    print(v_resultado[0])
elif len(v_resultado) == 3:
    print(v_resultado[0] + ' ' + v_resultado[2])
"""

print(v_resultado[0] + ' ' + v_resultado[len(v_resultado) - 1])
