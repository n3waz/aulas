nomes = []
sobrenomes = []
idades = []

quant = input('quantas pessoas deseja cadastrar? ')

for i in range(int(quant)):
    nomes.append(input('Insira o nome: '))
    sobrenomes.append(input('Insira o sobrenome: '))
    idades.append(input('Insira a idade: '))

arquivo = open('Atividades\Aulas\manipulacao.py\dados.txt', 'a', encoding='utf-8')

arquivo.write(f'Quantidade de cadastros: {quant}\n')

for i in range(int(quant)):
    arquivo.write('Nome: ' + nomes[i] + ' ' + sobrenomes[i] + ';Idade: ' + idades[i] + '\n')

arquivo.close()