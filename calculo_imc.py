peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC: {imc}, abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc}, peso normal.')
else:
    print(f'IMC: {imc}, acima do peso.')