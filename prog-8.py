peso = float(input("digite seu peso, em kg : "))
altura = float(input("digite sua altura, em m : "))
imc = peso / (altura**2)
print(f"seu imc eh {imc:.2f} pois seu peso eh {peso} e sua altura eh {altura}")
