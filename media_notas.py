# Crie um programa que leia 3 notas de um aluno e calcule a média dele.

notas = []

for  nota in range(1,4):
    notas.append(float(input(f'Digite a nota {nota}: ')))
    if nota == 3:
        media = sum(notas) / 3
        print(f'A média das notas é: {media}')
