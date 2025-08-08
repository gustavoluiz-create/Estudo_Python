preco = float(input("Digite o preço do produto - R$: "))
desco = preco - (preco * 0.05)
print(f"O preço do produto que originalmente custa: R$ {preco:.2f}, recebeu um desconto de 5% no seu valor")
print(f"Seu novo preço será: R${desco:.2f}")