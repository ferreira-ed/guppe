"""
Escopo de váriaveis

Dois casos de escopos:

1 - Váriaveis globais;
    - Váriaveis globais são reconhecida, ou seja, seu escopo compreende, todo o programa.

2 - Váriaveis locais;
    - Váriaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar váriaveis em python:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma váriavel, nós não colocamos o tipo de dado nela.
Este tipo é inferido ao atribuirmos valor a mesma

exemplo em C#:

int numero = 42;
"""

numero = 42 #Exemplo de váriavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 5

if numero > 10:
    novo = numero + 10  # A váriavel 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)

print(novo)

