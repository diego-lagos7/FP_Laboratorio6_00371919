def inicio ():
    opc = True
    contadorPares = 0

    while (opc):
        pedirNumeroPar = input("¿Desea ingresar un número impar? (S/N)")
        if (pedirNumeroPar == 'S'):
            numero = int(input("Escriba un numero par: ")) # Conversion de texto a número entero --> (string to int)
            if (numero % 2 == 0): 
                contadorPares += 1
            else:
                print("El número ingresado no es par. Intente otra vez.")
        else:
            opc = False

    print("Ha escrito " + str(contadorPares) + " numeros pares")

if __name__ == "__main__":
    inicio()
