"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not, o valor do booleano é invertido, ou seja, se for True vira False e vice-versa
Para o 'is', o valor é comparado com um segundo, comparando o valor real com o definido
"""
nome_usuario = input('Qual seu nome?')

ativo = True
logado = True

# Se não estiver ativo
if not ativo:
    print(f'Você precisa ativar sua conta{nome_usuario}, por favor cheque seu E-mail!')
else:
    print(f'Seja bem-vindo, {nome_usuario}!')

#Ativo é verdadeiro
print(ativo is True)
