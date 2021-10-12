#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

r = float(input('Quanto você tem na sua carteira: R$'))
d = r/5.39

print(f'Com R${r}, você pode comprar U${d:.2f}.')
