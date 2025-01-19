renda = float(input("Digite a renda mensal: "))
parcela = float(input("Digite o valor da parcela: "))

if parcela > renda * 0.3:
    print("Empréstimo negado: parcela acima de 30% da renda.")
else:
    print("Empréstimo aprovado.")