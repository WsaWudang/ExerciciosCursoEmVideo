#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input("Digite a quantidade de metros para ser convertido "))
mm = m *1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000

print(f"{m} metros tem \n"
	  f"{km} Quilômetros \n"
	  f"{hm} Hectômetro \n"
	  f"{dam} Decâmetro \n"
	  f"{dm} Decímetro \n"
	  f"{cm} Centímetro \n"
	  f"{mm} milímetros \n")
