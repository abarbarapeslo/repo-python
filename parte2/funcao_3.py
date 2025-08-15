'''
def salvar_carro(modelo,placa,ano):
    m = input(f'Informe o modelo do carro: ')
    p = input(f'Informe a placa do carro: ')
    a = input(f'Informe o ano do carro: ')
    print(f' Seu carro é {m}, placa {p} e ano {a} foi salvo com sucesso!')


while True:
    salvar_carro(modelo= 'm', placa= 'p', ano= 'a')  # Chamada da função com parâmetros nomeados
    continuar = input('Deseja continuar? (s/n): ')
    continuar = continuar.strip()  # Remove espaços em branco extras
    continuar = continuar.lower()  # Converte para minúsculas para comparação
    continuar = continuar[0]  # Pega apenas o primeiro caractere para comparação
    if continuar != 's':
        break

salvar_carro(modelo= 'm', placa= 'p', ano= 'a')  # Chamada da função com parâmetros nomeados
'''

def pergunta():
    info = input('Qual é o seu nome?: ')
    mens = input('Qual é a sua idade?: ')

    print(f'Seu nome é {info} e você tem {mens} anos!')

pergunta()