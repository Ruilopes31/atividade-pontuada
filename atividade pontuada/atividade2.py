import os

#solicitar dados do usuario

nome= input("digite seu nome:")
sexo= input("digite seu sexo (m) or(f):")
estado_civil= input("digite seu estado civi(SOLTEIRO, CASADO, DIVORCIADO, VIÚVO):")

#VERIFICAR O SEXO
if sexo == "f" and estado_civil== "casada":
    tempo_casada= int(input("digite o tempo de casada(em anos):"))

#mostrar dados
print("nome:", nome)
print("sexo:",sexo)
print("estado civil:",estado_civil)

#tempo de casada
if sexo == "f" and estado_civil == "casada":
    print("tempo de casada:", tempo_casada, "anos")