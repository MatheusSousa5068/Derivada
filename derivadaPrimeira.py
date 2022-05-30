'''
    Derivadas seguem a seguinte lógica:

    A derivada de x² é 2x¹
    A derivada de x³ é 3x²

    E assim em diante
'''

# Calcula o valor da derivada primeira
def derivadaPrimeira(valor):
    # Divide o valor inserido em "base" e "expoente"
    baseStr, expoenteStr = valor.split('x^')

    # Converte o expoente de string para integer e subtrai 1
    base = int(baseStr)
    expoente = int(expoenteStr)

    # Calcula os valores da derivada
    baseDerivada = base * int(expoenteStr)
    expoenteDerivada = expoente - 1

    derivada = str(baseDerivada) + 'x^' + str(expoenteDerivada)

    return derivada


#TODO: fazer funcionar com uma função inteira