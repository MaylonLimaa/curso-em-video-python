"""
Desafio 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
"""

veloc = float(input('Qual a velocidade do carro? '))
valormulta = (veloc - 80) * 7

if veloc > 80:
    print(f'Você foi multado! O valor é de R$ {valormulta}')
else:
    print('Está dentro do limite, sem multa!')

