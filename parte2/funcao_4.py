def exibir_poema(data_extenso, *args, **kwargs): #parametros de data_extenso, tupla e dicionario
    texto = '\n'.join(args) #os argumentos de args irão ficar cada um em uma nova linha

    #o dicionario kwargs ira receber os metadados e formatar cada chave e valor em uma nova linha
    meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()]) # items recebe uma lista de tuplas com   'chave'   e    'valor'

    #montando a mensagem final
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"

    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

# * representa tupla e ** dicionário

