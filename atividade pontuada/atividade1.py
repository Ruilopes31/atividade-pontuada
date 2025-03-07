import os
os.system("clear")

#solicitar dados
a=int(input("digite o valor de a:"))
b=int(input("digite o valor de b:"))
c=int(input("digite o valor de c:"))

if a + b < c:
    print("a + b é menor que c")
else:
    print("a + b é maior ou igual a c")   
