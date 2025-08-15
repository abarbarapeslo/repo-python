# upper() -> passar tudo dentro de uma string para maiúsculo
# lower() -> passar tudo dentro de uma string para minúsculo    
# title() -> passar a primeira letra de cada palavra para maiúsculo
# capitalize() -> passar a primeira letra da string para maiúsculo


# -> encurtando espaços de string

# strip() -> remove espaços no início e no final da string
# lstrip() -> remove espaços no início da string
# rstrip() -> remove espaços no final da string

# -> Junções e centralizações de string
# curso = "Python"
# join() -> junta uma lista de strings em uma única string, com um separador./ Exemplo: print('.'.join(curso)) -> "P.y.t.h.o.n"
# center() -> centraliza a string em um determinado tamanho, preenchendo com espaços./ Exemplo: print('Python'.center(10, '*')) -> **Python**

# OBS: O join é iteravel e passará igual ao for = item a item.


nome = "BaRbaRa"

print(nome.upper()) # BARBARA
print(nome.lower()) # barbara
print(nome.title()) # Barbara
print(nome.strip()) # BaRbaRa
print(nome.lstrip()) # BaRbaRa
print(nome.rstrip()) #   BaRbaRa
print('*'.join(nome.strip() + '.')) # *  *B*a*R*b*a*R*a.

print(nome.center(14)) #  BaRbaRa  
print(nome.center(14, '#')) # **BaRbaRa**