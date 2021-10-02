def f_calcula_notas(v_nota1, v_nota2):
    try:
        return ((int(v_nota1) + int(v_nota2)) / 2) #vai devolver o resultado da operação
    except:
        return 0
def f_inicializa_sistema ():
    v_numa = input('Digite a primeira nota: ')
    v_numb = input('Digite a segunda nota: ')
    v_resultado = f_calcula_notas(v_numa, v_numb)
    print(v_resultado)
f_inicializa_sistema()
