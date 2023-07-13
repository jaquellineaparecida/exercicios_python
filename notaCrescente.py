# Escreva um programa que leia 3 notas, calcule a média e imprima no console as notas ordenadas de forma crescente e a média obtida

print("MÉDIA")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
result = (nota1+nota2+nota3)/3

cresc = [nota1, nota2, nota3]
print("Suas notas são: " + str(sorted(cresc)) + str(result))