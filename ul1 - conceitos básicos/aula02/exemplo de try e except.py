#try - tratativa (sempre antes das variav e tal;) - o que eu quero executar; se caso não conseguir:
#except (exceção) - cai aqui.
"""
digamos que vamos dividir 10/0 = erro; quando se detecta um erro, é uma exceção. Se não conseguiu, gerará erro. É importante
para o usuário, justamente. Exemplo:
"""
v_numa = 8
v_numb = 0
v_resultado = 0
try:
    v_resultado = v_numa / v_numb
    print(v_resultado)
except:
    print('Erro ao dividir os números.')
