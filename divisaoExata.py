print("SAIBA SE A DIVISÃO É EXATA")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
result = num1 % num2

if result == 0:
    print("A divisão do " + str(num1) + " " + str(num2) + " é exata")

else:
    print("A divisão não é exata")
