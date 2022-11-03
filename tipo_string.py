"""
Tipo String

Um dado é considerado string sempre que tiver entre:
- aspas simples
- aspas duplas
- aspas simples triplas
- aspas duplas triplas

nome = 'Geek University'
print(nome)
print(type(nome))
print(nome.upper())

nome = "Gina's Bar"
print(nome)
print(type(nome))
print(nome.lower())

nome = 'Angelina Jolie'
print(nome.split())
# split separa a variavel nome em uma lista de strings
print(type(nome))
"""

nome = 'Geek University'
print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

print(nome.split()[0]) #Acessar um item através da lista de string que é formada pelo slice

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1]) #Inversão da string Pythônico

print(nome.replace('G', 'P')) #Substitui a letra G na váriavel pela letra P usando replace

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)
print(texto[::-1])

