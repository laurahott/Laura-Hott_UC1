dia = input("digite o dia da semana ")
match dia :
    case "seg" | "ter" | "qua" | "qui" | "sex" :
    # se for uma dessas opções, imprime oq ta adiante
        print("dia de semana !")
    case "sab" | "dom" :
        print("finde!")
    case _ :
        print("dia inválido")