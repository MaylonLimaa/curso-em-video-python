"""
Curso Python #06 - Tipos Primitivos e Saída de Dados

tipos primitivos:
Inteiro = int
Real = float
Booleano = Bool (Verdadeiro ou Falso)
String = str

Este arquivo mostra mais interações, como, bool, float, etc.
"""

I = int(input('Inteiro: '))
# Pede um dado para variável i e o converte em inteiro
print(type(I))
# Exibe o tipo deste dado
R = float(input('Real: '))
# Pede um dado para variável r e o converte em Real
print(type(R))
# Exibe o tipo deste dado
B = bool(input('Booleano: '))
# Pede um dado para variável b e o converte em Booleano
print(type(B))
# Exibe o tipo deste dado
S = str(input('String: '))
# Pede um dado para variável s e o converte em String
print(type(S))
# Exibe o tipo deste dado

n = input('Digite um número: ')
print(n.isnumeric())
# Verifica é possível converter de string para Int ou Float
print(n.isalpha())
# Verifica se n é composto por letras
print(n.isalnum())
# Verifica se N é alphanúmerico(Composto por letras e números)
