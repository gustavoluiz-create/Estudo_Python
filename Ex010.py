num = float(input("Digite o dinheiro que você tem em reais: "))

do = num / 5.46
euro = num / 6.36
libra = num / 7.33

print(f"Com R${num:.2f} você consegue comprar  U${do:.2f} ")
print(f"Com R${num:.2f} você consegue comprar  €{euro:.2f} ")
print(f"Com R${num:.2f} você consegue comprar  £{libra:.2f} ")