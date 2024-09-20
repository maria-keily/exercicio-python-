preco = float(input('Digite o preço original: R$ '))
desconto = float(input('Digite o desconto (%): '))

preco_final = preco - (preco*desconto / 100)

print(f"Preço com desconto: R$ {preco_final:.2f}")