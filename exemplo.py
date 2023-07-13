print("LEITOR DE MEDIA")
n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
n3 = float(input("Digite a terceira nota "))
media = (n1+n2+n3)/3

if media >= 9:
    conceito = "A"
    
elif media >= 8 and 8.9:
    conceito = "B"

elif media >= 7 and 7.9:
   conceito = "C"

elif media >= 6 and 6.9:
    conceito = "D"

else:
    conceito = "E"

match conceito:
    case "A":
        print("Sua média é " + str(media) + " conceito A")
    
    case "B":
        print("Sua média é " + str(media) + " conceito B")
    
    case "C":
        print("Sua média é " + str(media) + " conceito C")
    
    case "D":
        print("Sua média é " + str(media) + " conceito D")
    
    case "E":
        print("Sua média é " + str(media) + " conceito E")





