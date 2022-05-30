from utils import valorRaizes
from derivadaPrimeira import derivadaPrimeira

print('\033[1;34m=' * 26)
print(' Calculadora de derivadas')
print('=' * 26)

funcao = input('\033[1;96mInforme a função que deseja derivar (Exemplo de formato: 1x^2): ')
derivada = derivadaPrimeira(funcao)

print(f'A derivada de \033[1;31m{funcao} \033[1;34mé \033[1;95m{derivada}')