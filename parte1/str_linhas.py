#string de multiplas linhas utiliza-se """ ou ''' para formatar a string da forma que se deseja

nome = input('Digite seu nome: ')
mensagem = f''' 

    Olá, {nome}! Bem-vindo ao nosso sistema.
    Por favor, siga as instruções abaixo para continuar,

>> 1. Verifique seus dados.
>> 2. Atualize suas informações, se necessário.

                            
                            Se precisar de ajuda, entre em contato com o suporte.
'''

print(mensagem)