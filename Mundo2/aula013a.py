"""
Curso Python #013 - Estrutura de repetição for
"""

# ==============================
# 1. Loop simples em lista
# ==============================
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(f"Fruta: {fruta}")

print('-'*40)

# ==============================
# 2. Loop com índice usando range
# ==============================
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

print('-'*40)

# ==============================
# 3. Loop com enumerate (índice + valor)
# ==============================
for idx, fruta in enumerate(frutas):
    print(f"{idx}: {fruta}")

print('-'*40)

# ==============================
# 4. Loop sobre string (caractere a caractere)
# ==============================
nome = "Python"
for letra in nome:
    print(letra, end=' ')
print('\n' + '-'*40)

# ==============================
# 5. Loop com passo e inversão (usando range)
# ==============================
for num in range(10, 0, -2):  # do 10 até 1, passo -2
    print(num, end=' ')
print('\n' + '-'*40)

# ==============================
# 6. Loop sobre dicionário (chaves)
# ==============================
idades = {'Alice': 25, 'Bob': 30, 'Carol': 22}
for pessoa in idades:
    print(f"{pessoa} tem {idades[pessoa]} anos")

print('-'*40)

# ==============================
# 7. Loop sobre dicionário (chave e valor)
# ==============================
for pessoa, idade in idades.items():
    print(f"{pessoa} tem {idade} anos")

print('-'*40)

# ==============================
# 8. Loop aninhado (matriz ou combinação)
# ==============================
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # pular linha por linha da matriz

print('-'*40)

# ==============================
# 9. Loop com lista por compreensão (com for embutido)
# ==============================
quadrados = [x**2 for x in range(6)]
print("Quadrados:", quadrados)

# ==============================
# 10. Loop com break e continue
# ==============================
for num in range(10):
    if num == 5:
        break  # sai do loop
    if num % 2 == 0:
        continue  # pula o restante do bloco e vai para próxima iteração
    print(num, end=' ')
