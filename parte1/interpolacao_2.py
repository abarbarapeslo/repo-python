# interpolação com f-string ou format() utilizando o número da variável

PI = 3.14159

print(f'Valor de PI: {PI:.2f}') # f-string
print('Valor de PI: {:.2f}'.format(PI)) # format()

nome = 'Bárbara'
idade = 23

dados = {'Nome': nome, 'Idade': idade}

print(f'Nome: {nome}, Idade: {idade}') # f-string
print('Nome: {}, Idade: {}'.format(nome, idade)) # format()
print('Nome: {0}, Idade: {1}'.format(nome, idade)) # format() com índices
print('Nome: {name}, Idade: {age}'.format(name=nome, age=idade)) # format() com nomes de variáveis  
print('Nome: {Nome}, Idade: {Idade}'.format(**dados)) # format() com dicionário