x = input("Digite alguma coisa? ")

print(f"Possui somente números {x.isnumeric()}")
print(f"Possui somente letras? {x.isalpha()}")
print(f"Possui números ou letras? {x.isalnum()}")
print(f"Está capitalizada? {x.istitle()}")
print(f'Está em letras maiusculas? {x.isupper()}')
print(f'Está em letras minusculas? {x.islower()}')
print(type(x))