# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input("Quantos dias o carro foi alugado ? "))
kmp = float(input("Qauntos km foram rodados ? "))
pagar = (dia * 60) + (kmp * 0.15)

print(f"O total a pagar é de R${pagar:.2f}")