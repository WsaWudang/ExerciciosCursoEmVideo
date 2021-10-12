#Faça umprograma que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import sin, cos, tan, radians

angulo = float(input("Digite o anglo que deseja: "))

seno = sin(radians(angulo))#pegar o angulo converter em radiano depois o  angulo de radiano, calcula o seno
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"o angulo {angulo} tem o seno de {seno:.2f}\n"
    f"o angulo {angulo}, tem o cosseno {cosseno:.2f}\n"
    f"O angulo {angulo}, tem a tangente {tangente:.2f}")