v_valor = input('Informe o valor que deseja converter: ')
v_operacao = input('Deseja converter de Real para Dolar? Digite S para sim ou N para converter de Dolar para Real: ')

def f_converter_para_dolar(v_valor):
    return float(v_valor) * 5.23

def f_converter_para_real(p_valor):
    return float(p_valor) / 5.23
if v_operacao == 'S':
    print('Esse valor fica ' + str(f_converter_para_dolar(v_valor)) + ' dolar')
elif v_operacao == 'N':
    print('Esse valor fica ' + str(f_converter_para_real(v_valor)) + ' dolar')
else:
    print('Operador iformado inválido')
