larg = float(input("Digite a largura da parede (em metros): "))
altu = float(input("Digite a altura da parede (em metros): "))

area = larg * altu

print(f"A parede possui uma área {area:.2f}m²")
print(f"Para pintar toda a parede será necessário {area / 2}l de tinta")