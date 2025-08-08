dist = float(input("Quantos km você percorreu nessa viagem? Km: "))
dia = int(input("O carro foi alugado por quantos dias? "))

custo_dia = dia * 60
custo_dist = dist * 0.15
total = custo_dia + custo_dist

print(f"O preço total a pagar pela a quantidade de {dia} dia(s) e {dist} km(s) rodados são de R$: {total:.2f}")
