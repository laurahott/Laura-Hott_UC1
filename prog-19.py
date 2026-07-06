erro = input("digite o erro ")
match erro :
    case "200":
    # se for uma dessas opções, imprime oq ta adiante
        print("tudo certo!")
        
    case "400" :
        print("requisição mal formada")

    case "401" | "403" :
        print("não tem acesso a pág")

    case "404" :
        print("pág não encontrada")

    case "500" | "503" :
        print("sistema instável")

    case _ :
        print("esquisito desconhecido !!")