# Solicita as informações do usuário
produto = input("nome: ")
quantidade = int(input("Quantidade comprada: "))
preco = float(input("Preço unitário: "))

# Calcula o total
total = quantidade * preco

# Define o desconto com base na quantidade comprada
if quantidade <= 5:
    desconto = total * 0.02  # 2% de desconto
elif quantidade <= 10:
    desconto = total * 0.03  # 3% de desconto
else:
    desconto = total * 0.05  # 5% de desconto

# Calcula o total a pagar
total_pagar = total - desconto

# Exibe os resultados
print("\nResumo da compra:")
print("Produto:", produto)
print("Total: R$", format(total, ".2f"))
print("Desconto: R$", format(desconto, ".2f"))
print("Total a pagar: R$", format(total_pagar, ".2f"))
