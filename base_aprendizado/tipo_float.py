"""
Tipo Float

Tipo real, decimal

Casas decimais

obs: o seperador em casas decimais na programação é o ponto e não a vírgula
"""

#Errado do ponto de vista Float, mas gera uma tuple
valor = 1, 44
print(valor)
print(type(valor))


#Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

#É possivel fazer dupla atribuição
valor1, valor2 = 1.5, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Convertendo float para int
#Ao converter de float para inteiro, se perde precisão no resultado
res = int(valor)
print(res)
print(type(res))

#numeros complexos
variavel = 5j