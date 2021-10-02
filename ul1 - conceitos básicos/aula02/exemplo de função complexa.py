def f_soma (v_dados):
    v_soma = 0
    for item in v_dados:
        v_soma = (v_soma + float(item))

    return v_soma

def f_subtrai (v_dados):
    v_subtrai = 0
    for item in v_dados:
        v_subtrai = (v_subtrai - float(item))

    return v_subtrai

def f_divide (v_dados):
    v_divide = 0
    for item in v_dados:
        v_divide = (v_divide + float(item))

    try:
        return (v_divide / int(v_dados [- 1]))
    except:
        return 0

def f_multiplica (v_dados):
    v_multiplica = 0
    for item in v_dados:
        v_multiplica = (v_multiplica + float(item))

    return (v_multiplica * int(v_dados[-1]))

def f_calcula(v_dados, v_operador):
    if v_operador == '+':
        return f_soma(v_dados)
    elif v_operador == '-':
        return f_subtrai(v_dados)
    elif v_operador == '/':
        return f_divide(v_dados)
    elif v_operador == '*':
        return f_multiplica(v_dados)

def f_init ():
    v_operacao = input('Digite a operação: ')
    v_continua = 's'
    v_valores = []
    while v_continua == 's':
        v_valores.append(input('Digite o número: '))
        v_continua = input('Deseja continuar (s/n)')


    print('Valor é: ' + str(f_calcula(v_valores, v_operacao)))

f_init()
