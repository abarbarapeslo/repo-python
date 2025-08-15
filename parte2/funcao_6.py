#funçao de escopo global

salario = 1000  # Variável global

def calcular_bonus(bonus):
    global salario  # Declaração de variável global
    return bonus + salario * 0.10  # Variável local



calcular_bonus(100)  # Chamada da função
