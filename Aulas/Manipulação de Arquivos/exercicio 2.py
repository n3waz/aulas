cadastro = open('Atividades\Aulas\manipulacao.py\dados.txt', 'a', encoding='utf-8')

qtds = input('Quantos cadastros deseja fazer? ')

cadastro.write(f'Quantidade de cadastros: {qtds}\n')

for i in range(int(qtds)):
    nome = input('Nome: ')
    idade = input('Idade: ')
    cadastro.write(f'Nome: {nome};Idade: {idade}\n')

cadastro.close()