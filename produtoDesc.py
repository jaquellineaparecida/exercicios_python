produto = float(input("Digite o valor do seu produto: "))
qtd = int(input("Digite a quantidade que você comprou: "))
result = produto * qtd

if result >= 100 and 199:
    print("O valor total da sua compra e: " + str(result-(result*10/100)))

elif result >= 200 and 299:
    print("O valor total da sua compra e: " + str(result-(result*20/100)))

elif result >= 300 and 399:
    print("O valor total da sua compra e: " + str(result-(result*30/100))) 
elif result > 400:
    print("O valor total da sua compra e: " + str(result-(result*40/100)))

else:
    print("O valor total da sua compra e: " + str(result))