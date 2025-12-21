"""
Desafio 34: Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento. Para salários superiores a R$1.250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

sal = float(input('Qual o salário? '))

if sal > 1250:
    print(f'O valor do salário com aumento de 10% fica {sal * 1.1}')
else:
    print(f'O valor do salário com aumento de 15% fica {sal * 1.15}')