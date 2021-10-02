v_numero1 = 2
v_numero2 = 3
v_operador = '-'


def f_soma(p_n1, p_n2):
    print(p_n1 + p_n2)


def f_diminui(p_n1, p_n2):
    if p_n1 > p_n2:
        print(p_n1 - p_n2)
    else:
        print(p_n2 - p_n1)


if v_operador == '+':
    f_soma(v_numero1, v_numero2)

elif v_operador == '-':
    f_diminui(v_numero1, v_numero2)
