opcao = -1

while opcao != 0: #while executa até que a condição seja atendida
    opcao = int(input('Digite [1] para sacar, [2] para depositar ([0] para sair): '))
    if opcao == 1:
        print(f'Sacando...')
    elif opcao == 2:
        print(f'Depositando...')
    elif opcao < 0 or opcao > 2:
        print(f'Opção inválida, tente novamente.')
    elif opcao == 0:
        print(f'Encerrando...')