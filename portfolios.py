projetos   = ['Website', 'Jogo','análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    if projeto is None:
        print('Projeto ausente')
        continue
    print(projeto)