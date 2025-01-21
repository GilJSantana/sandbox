
for segundo in reversed(range(1,11)):
    if segundo % 2 == 0:
        print(f'Faltam apenas {segundo} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {segundo} segundos restantes...')
print('Aproveite a promoção agora!')