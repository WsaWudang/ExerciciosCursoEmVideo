#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = float(input("Informe a temperatura em °C: "))
fahrenheit = celcius * 1.8 + 32

print(f"A temperatura de {celcius}°C corresponde a {fahrenheit}°F!")
