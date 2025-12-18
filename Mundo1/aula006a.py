"""
Curso Python #06 - Tipos Primitivos e Saída de Dados

tipos primitivos:
Inteiro = int
Real = float
Booleano = Bool (Verdadeiro ou Falso)
String = str

Neste arquivo mostra principalmente, interações com números.
"""

n1 = input('Digite um número: ')
# Recebe um valor para n1
print(type(n1))
# Imprime o tipo primitivo de n1, neste caso, String
n1 = int(n1)
# Converte n1 para inteiro
print(type(n1))
# Imprime o tipo primitivo de n1, neste caso, int
n1 = int(input('Digite um número: '))
# O método int() converte uma String para Inteiro
n2 = int(input('Digite um outro número: '))

s = n1 + n2
# Variável s recebe dois valores inteiros e os soma
print(f'A soma entre {n1} e {n2} é igual a {s}')
