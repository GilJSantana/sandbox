macas = int(input('Quantas maçãs você vendeu?\n'))
bananas = int(input('Quantas bananas você vendeu?\n'))

if macas > bananas:
    print('Vendeu mais maçãs.')
elif bananas == macas:
    print('Vendeu a mesma quantidade de maçãs e bananas.')
else:
    print('Vendeu mais bananas.')