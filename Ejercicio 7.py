def main ():
    numero = input ("Numero: ")
    longitud = len(numero)

    salida = ""

    for i in range(0, longitud):
        salida += numero[(longitud - 1) - i]

    print ("El numero es: " + salida)

if __name__ == '__main__':
    main()
