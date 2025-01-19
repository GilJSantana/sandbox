despesas = float(input('Digite o total de despesas do mês (R$): '))
limite = 3000

if despesas>limite:
    print('Atenção! Você ultrapassou o limite do orçamento!')
else:
    print('Despesas dentro do limite do orçamento!')
