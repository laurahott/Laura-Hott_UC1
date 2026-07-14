# dados valores de produtos, soma os valores + 10% e nos dá o valor da conta final
# digitando 0 acaba



# variável. pede o valor do produto. int pq o valor só pode ser inteiro
valor = 1

# variável acumuladora. começa em zero pq num recebeu nada ainda. ela soma os valores dos produtos escolhidos
total = 0

while valor != 0:  # enquanto o valor for diferente de zero, executa

    # pede valor pra continuar
    valor = int(input("digite o valor: "))

    total = total + valor

print(f"o total das compras com 10% eh {total * 1.1}")