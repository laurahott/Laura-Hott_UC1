cargo = input("digite seu cargo ")
if cargo == "caixa":
    salario = 1500
elif cargo == "vendedor":
    salario = 2400
elif cargo == "gerente":
    salario = 4000
else :
    salario = 0
    print("cargo num existe")

inss = salario * 0.12
if salario > 2000 :
    irrf = salario * 0.14
else :
    irrf = salario * 0.08

salario_final = salario - inss - irrf
print(f"seu cargo de {cargo} tem salário {salario},inss {inss}, irrf {irrf} e seu salário final eh {salario_final}")

