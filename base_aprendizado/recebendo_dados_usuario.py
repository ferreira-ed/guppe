"""
recebendo dados do usuario

input() -> todo dado recebido via input é do tipo string
"""

#Entrada de dados mais "antiga":
#print('Qual seu nome?')
#nome = input() #input -> Entrada

#print('Qual sua idade?')
#idade = input()

#Entrada de dados versão 3.x
nome = input('Qual seu nome?')

idade = int(input('Qual sua idade?'))

"""
int(input) => Cast

Cast é a conversão de um tipo de dado para o outro, no caso o input vem como string fizemos a conversao
do valor para int
"""

#Exemplo de print antigo 2.x
#print('Seja bem vindo (a) %s' % nome)

#Exemplo de print moderno 3.x
#print('Seja bem vindo (a) {0}'.format(nome))

#Exemplo de print atual 3.7
print(f'Seja bem vindo (a),{nome}')

#Saída

#Exemplo de print antigo 2.x
#print('A %s tem %s anos' % (nome, idade))

#Exemplo de print moderno 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

#Exemplo de print atual 3.7
print(f'A {nome} tem {idade} anos')

print(f'A {nome} Nasceu em {2022 - idade}')






