#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o valor do sálario a ser acrescentado 15% ? "))

print("Um funcionario quue ganhava R${salario}, Com 15% de aumento, passou a receber R${:.2f} reias".format(salario+(salario*0.15)))

