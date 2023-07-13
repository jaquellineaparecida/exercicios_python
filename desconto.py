produto = float(input("Digite o valor do seu produto: "))
qtd = int(input("Digite a quantidade de produtos que você comprou: "))
result = produto * qtd
if produto >= 100.00:
    print("O valor final do seu produto é " + str((result * 10)/100))
else:
    print("O valor do produto é " + str(result))
