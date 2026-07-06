#digite 2 numeros e mostre o menu :
#1 - somar, 2 - subtrair, 3- multiplicar, 4 - dividir
#para imprimir texto com aspas, escrever : '("texto")'
n1 = int(input("fala o valor "))
n2 = int(input("fala outro "))
n1 = int(input("fala o valor: "))
n2 = int(input("fala outro: "))

print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")

escolha = input("digite uma das opções acima para operação: ")

match escolha:
    case "1":
        operacao = n1 + n2

    case "2":
        operacao = n1 - n2

    case "3":
        operacao = n1 * n2

    case "4":
        if n2 != 0:
            operacao = n1 / n2
        else:
            operacao = "erro: divisão por zero"

    case _:
        operacao = "opção inválida"

print(f"o resultado da operação eh {operacao}")