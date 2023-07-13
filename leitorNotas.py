print("LEITOR DE MEDIA")
n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
n3 = float(input("Digite a terceira nota "))
media = (n1+n2+n3)/3

if media >= 9:
    print("Sua média é " + str(media) + " com o conceito A")

elif media >= 8 and 8.9:
    print("Sua média é " + str(media) + " com o conceito B")

elif media >= 7 and 7.9:
    print("Sua média é " + str(media) + " com o conceito C")

elif media >= 6 and 6.9:
    print("Sua média é " + str(media) + " com o conceito D")

elif media < 6:
    print("Sua média é " + str(media) + " com o conceito E")

else:
    print("Você foi reprovado")
    




