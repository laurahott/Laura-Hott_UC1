menu = int(input("digite dois números: " , x , y))
match menu :    
    case x | y :
    total = x - y

    case "2" | "3" :
    total = x - y

    case "3" | "4" :
    total = x * y

    case "1" | "3" :
    total = x / y
print total

  