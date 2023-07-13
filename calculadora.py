n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input("Digite a operação que desaja fazer (+, -, *, /, **): ")

if operacao == "+":
    print("A soma de " + str(n1) + str(n2) + " é igual a: " + str(n1+n2))

elif operacao == "-":
    print("A subtração de " + str(n1) + str(n2) + " é igual a: " + str(n1-n2))

elif operacao == "*":
    print("A multiplicação de " + str(n1) + str(n2) + " é igual a: " + str(n1*n2))

elif operacao == "/":
    print("A divisão de " + str(n1) + str(n2) + " é igual a: " + str(n1/n2))

elif operacao == "**":
    print("A exponenciação de " + str(n1) + str(n2) + " é igual a: " + str(n1**n2))

else:
    print("Você inseriu uma operação que não pode ser realizada,tente novamente!")
