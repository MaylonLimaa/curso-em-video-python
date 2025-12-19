"""
Curso Python #09 - Manipulando Texto

Fatiamento usando a String como uma lista
"""

FRASE = 'Curso em Video Python'
# Em maisculo para indicar que se trata de uma constante

print(FRASE[5:10])
# Mostra todos os caracteres do indice 5 ao indice 9
print(FRASE[:10])
# Mostra todos os caracteres do indice 0 até o indice 9
print(FRASE[5:])
# Mostra todos os caracteres do indice 5 até o indice 20
print(FRASE[5:15:2])
# Mostra todos os caracteres do indice 5 até 14 porém pulando de 2 em 2
print(FRASE[5::2])
# Mostra todos os caracteres do indice 5 até o indice 20 pulando de 2 em 2
print(FRASE[::-1])
# Dois parametros vazios para usar todos os indices, passo negativo para começar do 20 até o 0
