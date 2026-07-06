nome = input("digite seu nome : ")
notasbi1 = float(input("digite e nota 1: "))
notasbi2 = float(input("digite e nota 2: "))
notasbi3 = float(input("digite e nota 3: "))
notasbi4 = float(input("digite e nota 4: "))

media = (notasbi1+notasbi2+notasbi3+notasbi4) / 4
print("sua média é: ", (media))

if media >=6 :
    print("aprovado")
else :
    print("recuperação")