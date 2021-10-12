#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("Digite Qualquer coisa: ")

print(f"O tipo primitivo desse valor é {type(a)} \n"
      f"Só tem espaços? {a.isspace()} \n"
      f"é somente números ? {a.isnumeric()} \n"
      f"É alfabético? {a.isalpha()} \n"
      f"Tem letras e números ? {a.isalnum()} \n"
      f"Está só em maiúsculas? {a.isupper()} \n"
      f"Está só em minúsculas? {a.islower()} \n"
      f"Tem letras maiúsculas e minúsculas ? {a.istitle()}")