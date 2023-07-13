print("DESCUBRA O SEU GRAU DE OBESIDADE(IMC)")
peso = float(input("Digite o seu peso "))
altura = float(input("Digite a sua altura "))
massa = peso / (altura*altura)

if massa <= 18.5:
    print("Você está com peso baixo")

elif massa <= 26:
    print("Você está em uma situação normal")

elif massa >= 26 and 30:
    print("Você está obeso")

elif massa >= 20:
    print("Você está com obesidade mórbida")