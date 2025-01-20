estoque = 5

def vender(qtd):
    global estoque
    if qtd > estoque:
        print('Estoque insuficiente!')
    else:
        estoque -= qtd

while estoque > 0:
    print(f'Venda realizada! Estoque restante: {estoque}')
    if estoque > 0 :
        livros_vendidos = int(input('Quantos livros foram vendidos? '))
        vender(livros_vendidos)

print('Estoque esgotado!')