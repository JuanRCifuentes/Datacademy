def es_adulto():
    edad = int(input("Escribe tu edad: "))
    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

def mayor_a_5():
    numero = int(input('Escribe un numero: '))

    if numero < 5:
        print('Es menor que 5')
    elif numero == 5:
        print('Es igual a 5')
    else:
        print('Es mayor que 5')

if __name__ == '__main__':
    es_adulto()
    mayor_a_5()