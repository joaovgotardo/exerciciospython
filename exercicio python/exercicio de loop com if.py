def soma_numeros():
    v_inicio = 1
    v_final = 10
    while v_inicio <= v_final:
        print(v_inicio)
        v_inicio = v_inicio + 1
    v_nome = input("Digite o seu nome: ")
    if v_nome == "Joelma":
        print("Parabéns")
    else:
        print("Não conheço")
soma_numeros()


