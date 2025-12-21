"""
Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 para viagens mais longas.
"""

dist = int(input('Quantos KM foram percorridos na viagem? '))
valorpassagem = (dist * 0.5) if dist <= 200 else (dist * 0.45)

print(f'O valor da passagem é de R$ {valorpassagem}')
