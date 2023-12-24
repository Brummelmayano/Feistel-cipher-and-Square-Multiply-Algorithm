def square_and_multiply(x, b, n):
    result = 1
    b_binary = bin(b)[2:][::-1]  # Conversion de b en binaire et inversion de la chaîne

    for bit in b_binary:
        result = (result ** 2) % n  # Carré à chaque itération

        if bit == '1':
            result = (result * x) % n  # Multiplication si le bit est égal à 1

    return result
