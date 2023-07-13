print("CONTA DE CONSUMO DE ENERGIA ELÉTRICA")

valor_minimo = 11.90
consumo = int(input("Digite a quantidade de KW que você consumiu: "))

if consumo <= 150:
   total = consumo * 0.20

elif consumo >= 150 and consumo < 500:
    total = consumo  * 0.25

else:
    total = consumo  * 0.30

if total > valor_minimo:
    print(f"Total a pagar: {valor_minimo:.2f}")

else:
    print("Total a pagar: " + str(total))

