"""
Curso Python #11 - Cores no Terminal
Padrão ANSI: \033[style;text;backm

Style (Estilo):
0 = None (Sem estilo)
1 = Bold (Negrito)
4 = Underline (Sublinhado)
7 = Negative (Inverte cores de texto e fundo)

Text (Cores de Texto):
30 = Branco      34 = Azul
31 = Vermelho    35 = Roxo
32 = Verde       36 = Ciano
33 = Amarelo     37 = Cinza

Back (Cores de Fundo):
40 até 47 (Mesma ordem das cores de texto acima)
"""

vermelho1 = '\033[0;31;46m'
vermelho2 = '\033[0;31;45m'
fimasc = '\033[m'
print('\033[0;32;40m testando testando \033[m')
print(f'{vermelho1} teste1 {fimasc} e {vermelho2} teste2 {fimasc}')
