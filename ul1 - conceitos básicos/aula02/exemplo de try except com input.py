v_numa = 0
v_numb = 0
v_resultado = 0

try:
   v_numa = int(input('Digite o primeiro número: '))
   v_numb = int(input('Digite o segundo número: '))
   v_resultado = (v_numa) / (v_numb)
   print('Resultado: ' + str(v_resultado))
except:
    print('Erro na operação')
