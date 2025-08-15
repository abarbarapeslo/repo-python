limite = int(input('Digite um número para ser o limite da contagem: '))

print(f"Contando de 0 até {limite-1}, mas pulando o 10...") 
#limite-1 para mostrar o número correto do range que vai até o número digitado menos 1

for i in range(limite): #para números de 0 até o 'limite' -> (digitado pelo usuário)
    if i == 10: # se o número for igual a 10
        continue # pule o 10
    print(i, end=" ") #print o número na mesma linha, separado por espaço
