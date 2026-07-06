from datetime import datetime

anonasc = int(input("digite seu ano de nascimento: "))
anoatual = datetime.now() .year
idade = anoatual - anonasc
print(f"você tem {idade} anos.")

if idade >= 18 :
    print("maior de idade")
else :
    print("menor de idade")