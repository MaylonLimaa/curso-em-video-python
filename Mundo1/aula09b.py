"""
Curso Python #09 - Manipulando Texto

Manipulando string com funções

"""

frase = 'Curso em Video Python'

print(len(frase))
# Função len() mostra quantos caracteres temos na frase
print(frase.count('o'))
# Função count() conta quantas vezes ele localiza o parametro
print(frase.count('o', 0, 13))
# Desta forma, ele vai procurar apenas do indice 0 até o 13
print(frase.find('deo'))
# A função find() localiza onde iniciou o parametro
print(frase.find('Android'))
# Como não há essa frase na String, retorna -1
print('Curso' in frase)
# Retorna True caso encontre e False se não localizar
print(frase.replace('Python', 'Android'))
# Procura Python e altera para Android
print(frase.upper())
# Deixa a String em maisculo(uppercase)
print(frase.lower())
# Deixa a String em minusculo(lowercase)
print(frase.capitalize())
# Deixa a String Capitalizada
print(frase.title())
# Deixa a String em formato de titulo

frase2 = '   Aprenda Python  '
print(frase2.strip())
# Remove os espaços no inicio e final da String
print(frase2.rstrip())
# Remove os espaços apenas ao final da String(r = right)
print(frase2.lstrip())
# Remove os espaços do inicio da String(l = left)

print(frase.split())
# Separa a String com cada palavra sendo uma lista
print('-'.join(frase))
