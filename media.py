nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
nota3=int(input("Digite a terceira nota: "))
result=int((nota1 + nota2 + nota3)/3)
if result <= 4:
    print("Sua nota é: " + str(result) + " Voce esta reprovado")
elif result >= 5:
    print("Sua nota e: " + str(result) + " Voce esta aprovado")
elif result == 10:
    print("Sua nota e: " + str(result) + " Voce foi aprovado com exito!")

