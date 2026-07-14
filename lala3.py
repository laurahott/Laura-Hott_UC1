# variável. ela pede pra vc falar o código do produto. o código vale um produto, que vale um valor 
codigo = int(input("digite o código do produto: "))  


# variável acumuladora. começa em zero pq num recebeu nada ainda. ela soma os valores dos produtos escolhidos
compras = 0 


while codigo != 0: # enquanto o código difere de zero, executa :

    if codigo == 1:
        print("001 -> arroz -> R$ 4")
        compras = compras + 4 # a variável compras vai somando seu valor i com o valor 4

    elif codigo == 2:
        print("002 -> feijão -> R$ 7")
        compras = compras + 7 # a variável compras vai somando seu valor i com o valor 7

    elif codigo == 3:
        print("003 -> macarrão -> R$ 5")
        compras = compras + 5 # a variável compras vai somando seu valor i com o valor 5

    else:
        print("inválido")

    codigo = int(input("digite outro código ou 0 para encerrar: "))

print(f"a soma total das compras eh R$ {compras}")