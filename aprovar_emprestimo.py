renda = float(input("Digite a renda mensal: "))
parcela = float(input("Digite o valor da parcela: "))

if renda > 2000 and parcela <= renda * 0.3:
    print("Empréstimo aprovado!")
elif renda <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")
