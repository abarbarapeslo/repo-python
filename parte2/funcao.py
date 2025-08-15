# é um bloco de código que contém uma identificação   'nome_da_funcao'   e   '(parametros)'   que indica que faz parte de uma função
# inicia como ->    def nome_da_funcao(parametros):

#funções declaradas
def identificador():
    print('Olá mundo!')

def identificador_2(parametro):
    print(f'Seja bem-vindo(a)! {parametro}')

def identificador_3(parametro='Bárbara'):
    print(f'Seja bem-vindo(a)! {parametro}, tudo bem?')


#chamando as funções
identificador()  # Chamada da função sem parâmetros
identificador_2('Bárbara')  # Chamada da função com um parâmetro
identificador_3()
identificador_3('João')  # Chamada da função com um parâmetro diferente descartando o parametro definido incialmente



