abecedario = 'abcdefghijklmnopqrstuvwxyz_'

def getRotor(n):

    rotorDinamico = []

    while n != 1:

       if n%2 == 0:

            n = n/2 

            rotorDinamico.append(n)

       else:

            n = n*3+1

            rotorDinamico.append(n)

    rotorDinamico = rotorDinamico+ rotorDinamico + rotorDinamico+ rotorDinamico+rotorDinamico+rotorDinamico +rotorDinamico +rotorDinamico

    return rotorDinamico

def cifrar(cadena, keyNumber):

    rotorDinamico = getRotor(len(cadena))
    textoCifrado = ''

    rotacion = 0

    for letra in cadena:

        suma = abecedario.find(letra) + rotorDinamico[rotacion] + keyNumber

        rotacion += 1

        modulo = int(suma) % len(abecedario)

        textoCifrado = textoCifrado + str(abecedario[modulo])

    return textoCifrado

def descifrar(cadena, keyNumber):

    rotorDinamico = getRotor(len(cadena))

    textoDescifrado = ''

    rotor = 0

    for letra in cadena:

        suma = abecedario.find(letra) - rotorDinamico[rotor] - keyNumber

        modulo = int(suma) % len(abecedario)

        textoDescifrado = textoDescifrado + str(abecedario[modulo])

        rotor += 1

    return textoDescifrado

def main():

    mensajeCifrar = input('cadena a cifrar: ').lower()

    palabraClave = input( "Introduce la palabra clave: ").lower()

    for letra in palabraClave:
        keyNumber = abecedario.find(letra)
        mensajeCifrar = cifrar(mensajeCifrar, keyNumber)
    
    print("Su mensaje encriptado es: ", mensajeCifrar)

    mensajeDescifrar = input('cadena a decifrar: ').lower()

    palabraClave = input( "Introduce la palabra clave: ").lower()

    for letra in palabraClave:
        keyNumber = abecedario.find(letra)
        mensajeDescifrar = descifrar(mensajeDescifrar, keyNumber)
        print(mensajeDescifrar)
    
    print("Su mensaje desencriptado es: ", mensajeDescifrar)

if __name__ == '__main__':

    main()