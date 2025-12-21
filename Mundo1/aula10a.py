"""
Curso Python #10 - Condições (Parte 1)
"""

idade = int(input('Quantos anos tem seu carro? '))

if idade <= 3:
    print('Carro novo')
else:
    print('Carro velho')

print('Carro velho' if idade>2 else print('Carro Novo'))
# If simplicado, equivalente a operador ternário de outras linguagens
