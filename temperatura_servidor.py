temperatura_atual = int(input('Informe a temperatura atual do servidor: '))

if temperatura_atual > 25:
    print('Alerta! Temperatura está acima do limite permitudo.')
else:
    print('Temperatura está dentro do limite permitido.')