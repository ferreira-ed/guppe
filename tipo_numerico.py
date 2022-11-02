"""
Tipo numerico

"""

#Variavel recebe valor e realiza a operação
num = 5
print(num / 2)

#Variavel recebe valor e converte o resultado da operação em inteiro
print(num // 2)

#objeto type identifica a classe da variavel
print(type(num))

#sinal de "+=" representa a adição do numero 1 na variavel num
num += 1

#subtração
num -= 1

#multiplicação
num *= 2

#divisão
num /= 2

#divisão terminada em inteiro
num //= 2
print(num)
print(type(num))

#definição que tambem funcionaria
num = num + 1

#usar underline em numeros extensos para melhor identação
novo_numero = 1_000_000

print(novo_numero)

#operação para adicionar um valor em python atraves do __add__
print(novo_numero.__add__(10_000))
