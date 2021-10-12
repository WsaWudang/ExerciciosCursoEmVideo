#um professor quer sortear um dos seus quarto alunos para apagar o quadro.
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice

nome1 = str(input('Primeiro aluno:'))
nome2 = str(input('Segundo aluno:'))
nome3 = str(input('Terceiro aluno:'))
nome4 = str(input('Quarto aluno:'))

lista = choice([nome1, nome2, nome3, nome4])

print(f"O aluno escolhido foi: {lista}")

