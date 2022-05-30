# Achar raízes
def valorRaizes(a, b, c):
    # Formula para achar o valor de delta
    delta = (b ** 2) - (4 * a * c)

    # Achar raizes da função
    x1 = ((-b) - (delta ** 1/2)) / (2 * a)
    x2 = ((-b) + (delta ** 1/2)) / (2 * a)

    return x1, x2