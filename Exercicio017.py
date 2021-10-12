#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa 

import math

def jeito1():
    print('Calculando a Hipotenusa')
    a = float(input('Insira o valor do cateto oposto: '))
    b = float(input('Insira o valor do cateto adjacente: '))

    hip = (a ** 2) + (b ** 2) #
    hip = sqrt(hip)

    print('A hipotenusa desse triângulo é:{:.2f}'.format(hip))

print('Calculando a Hipotenusa')
a = float(input('Insira o valor do cateto oposto: '))
b = float(input('Insira o valor do cateto adjacente: '))
hip = math.hypot(a, b)
print("A hipotenusa vai medir {:.2f}".format(hip))