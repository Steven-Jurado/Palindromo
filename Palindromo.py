def esPalindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabraInvertida == palabra:
        return True
    else:
        return False


def main():
    palabra = input('Ingrese la palabra:\n')
    if esPalindromo(palabra):
        print('FELICITACIONES, TIENES UNA PALABRA PALÍNDROMO👨‍💻👨‍💻')
    else:
        print('OUPS, NO ES UNA PALABRA PALÍNDOMO')


if __name__ == '__main__':
    main()
    