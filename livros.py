livros = [  'O Hobbit',
          'Dom Quixote de la Mancha',
          'Orgulho e Preconceito',
          'Metamorfose',
          'Crime e Castigo',
          'O Pequeno Príncipe',
          'O Alienista',
          'O Silêncio dos Inocentes',
          'Assassinato no Expresso do Oriente',
          'As Aventuras de Sherlock Holmes',
          'Não Conte a Ninguém',
          'É Assim que Acaba',
          'É Assim que Começa',
          'A Biblioteca da Meia Noite',
          'Verity',
          'Tudo é Rio',
          'Empregada']

for livro in livros:
    if livro == 'O Hobbit':
        posicao = livros.index('O Hobbit') + 1
        print(f'O Hobbit está na lista, encontra-se na posição: {posicao}')
        break