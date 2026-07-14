senha_correta = "python123" 
tentativas = 0 #começa em 0
max_tentativas = 3

while tentativas < max_tentativas :
    tentativa = input(f"digite a senha (tentativa {tentativas + 1}/{max_tentativas}): ") # pra cada tentativa aparece 1/3. 2/3. 3/3 tentativas
    
    if tentativa == senha_correta : # = atribui coisa à variável. == significa que vale um valor mesmo
        print (" acesso concedido ")
        break # cabô aí
    
    else :
        print( "senha incorreta")
        tentativas += 1

else :
    print("vc excede o número máx de tentativas. acesso bloqueado")