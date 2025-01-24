
quantidade_de_caracteres_nome = 0
quantidade_de_caracteres_senha = 0

def tamanho_nome_senha():
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    quantidade_de_caracteres_nome = len(usuario)
    quantidade_de_caracteres_senha = len(senha)
    return quantidade_de_caracteres_nome, quantidade_de_caracteres_senha


while quantidade_de_caracteres_nome <= 5 or quantidade_de_caracteres_senha <= 8:
    quantidade_de_caracteres_nome, quantidade_de_caracteres_senha = tamanho_nome_senha()

    if quantidade_de_caracteres_nome <= 5:
        print('Seu nome de usuário deve ter no mínimo 5 caracteres.')

    if quantidade_de_caracteres_senha <= 8:
        print('A senha deve ter no mínimo 8 caracteres.')


print('Cadastro realizado com sucesso!')