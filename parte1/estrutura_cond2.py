conta_normal = False
conta_universitaria = False

saldo = 1600
saque = 1500
cheque_especial = 600

if conta_normal:
    if saldo >= saque: #se o saldo for maior ou igual ao saque, realize
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial): # se não, saque é menor ou igual ao saldo+cheque
        print("Saque realizado com uso do cheque especial!") # saque + cheque especial
    else: #se não, não é possível realizar o saque
        print("Não foi possível realizar o saque.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")

else:
    print ("O sistema não reconheceu a conta informada.")

# if dentro de uma estrutura if = if aninhada