sexo = input("digite seu sexo: ").upper()
idade = int(input("digite sua idade: "))
print(f"sexo {sexo} idade {idade}")
if sexo == "M" and idade>=18 :
    print("apto")
else :
    print("não apto")
