
def somar(a,b):
    return a + b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a, b) #chamando a função que foi passada como argumento
    print(f'O resultado da operação {a} + {b} é: {resultado}')


exibir_resultado(20, 20, somar) #somar substitui a função passada como argumento -> funcao

op = somar

print(op(10, 5)) #chamando a função somar através da variável op
print(type(op)) #mostra que op é uma função