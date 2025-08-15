maior_idade = 18
idade_espacial = 12

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")

#if idade < maior_idade:
    #print("Você é menor de idade!")


if idade >= maior_idade:
    print("Você é maior de idade!")
elif idade == idade_espacial:
    print("Você é um alienígena!")
else:
    print("Você é menor de idade!")