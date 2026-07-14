
número = 1 # variável. omeça com 1 só pro while aceitar pq já eh mencionado 0 logo adiante. o programa soma números e pára se digitar 0.
           # a variável número passa a guardar o número que a pessoa digitou.
soma = 0  # variável. começa em zero porque ainda não somamos nada. o novo valor de soma vai ser o valor antigo de soma mais o valor de número.

while número != 0:
    número = int(input("digite o número: "))
    soma = soma + número # vai acumulando a soma.

print(f"a soma total eh {soma}")

### exemplo ###
# número = 5
# soma = soma + número
# soma = 0 + 5
# soma = 5

### daí ###
# número = 3
# soma = soma + número
# soma = 5 + 3
# soma = 8

