distancia = float(input('Qual a distância a ser percorrida (em KM): '))

if distancia <= 100:
    print('Valor do pedágio: R$ 10,00')
elif 100 <= distancia <= 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')
