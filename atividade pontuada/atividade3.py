import os
os.system("clear")

#solicitar dados
a=int(input("digite o valor de a:"))
b=int(input("digite o valor de b:"))

if a == b:
#se os valores forem iguais somamos a e b
    c = a + b
else:
# se forem diferentes multiplicamos a por b    
    c = a * b 

print("o resultado é:", c)