atividade_a = int(input('Informe os dias para a atividade A: '))
atividade_b = int(input('Informe os dias para a atividade B: '))
atividade_C = int(input('Informe os dias para a atividade C: '))

if atividade_a < 0 or atividade_b < 0 or atividade_C < 0:
    print('Erro: Os dias não podem ser negativos.')
else:
    tempo_total = atividade_a + atividade_b + atividade_C
    print(f'O tempo total das atividades é de {tempo_total} dias.')