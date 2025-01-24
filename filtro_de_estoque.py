livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

def filtro_de_estoque(livros):
    for livro in livros:
        if livro["estoque"] > 0:
            print(f'Livro disponível: {livro["nome"]}')

filtro_de_estoque(livros)