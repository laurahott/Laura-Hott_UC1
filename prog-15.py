ingresso = input("digite se tem ou não: ").upper()
idade = int(input("digite sua idade: "))
print(f"ingresso {ingresso} idade {idade}")
if ingresso == "S" and idade >= 12 :
    print("entra no parquinho")
elif ingresso == "S" or  ingresso == "N" and idade < 12 :
    print("não entra no parquinho")
else :
    print("não entra")