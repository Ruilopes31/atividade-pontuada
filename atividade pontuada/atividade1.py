import os
os.system("clear")

#solicitar dados
numero_um=int(input("digite o valor de a:"))
numero_dois=int(input("digite o valor de b:"))
numero_tres=int(input("digite o valor de c:"))

soma= numero_um + numero_dois

if soma>numero_tres: 
    print("primeiro numero e segundo maior que o terceiro numero")

else:
    print("terceiro numero maior que um e dois") 

print(f"numero um escolhido: {numero_um}") 
print(F"NUMERO DOIS ESCOLHIDO: {numero_dois}")
print(f"numero tres escolhido: {numero_tres}")
    
