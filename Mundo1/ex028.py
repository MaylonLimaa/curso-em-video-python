"""
Desafio 28: Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

NUM = randint(0, 5)
NUMUSUARIO = int(input('Digite um número entre 0 a 5: '))

if NUM == NUMUSUARIO:
    print(f'Parabéns você acertou! O número realmente era {NUM}')
else:
    print(f'Infelizmente você errou! O número era {NUM} e não {NUMUSUARIO}')
