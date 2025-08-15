# fatiamento de string é o processo de dividir uma string em partes menores, ou acessar partes específicas dela.

nome = 'Bárbara Lopes Vieira da Silva'

print(nome[0])
print(nome[:10]) # do início até o índice 9
print(nome[:10:14]) # do início até o índice 9, pulando de 14 em 14
print(nome[10:14:2]) # do índice 10 até o índice 13, pulando de 2 em 2
print(nome[:]) # toda a string
print(nome[::-1]) # string invertida (começa do fim para o início)