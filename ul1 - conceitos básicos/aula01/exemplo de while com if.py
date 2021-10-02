v_contador = 0
while (v_contador < 10):
    if (v_contador == 5 or v_contador == 3 or v_contador >= 7):
        print('Achou o numero: ' + str(v_contador))
    else:
        print('Numero nao encontrado: ' + str(v_contador))
    v_contador = v_contador + 1
