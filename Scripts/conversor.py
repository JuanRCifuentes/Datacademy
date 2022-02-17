def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f'Cuantos pesos {tipo_pesos} tienes?'))
    dolares = round(pesos / valor_dolar, 2)
    print(f'Tienes ${dolares} {"dolares" if dolares>1 else "dolar"}')

def main():
    menu = """
    Buenvenido al conversor de monedas 💲

    1 - Pesos Colombianos
    2 - Pesos Argentinos
    3 - Pesos Mexicanos

    Elige una opcion: """

    opcion = int(input(menu))

    if opcion == 1:
        conversor('colombianos', 4000)
    elif opcion == 2:
        conversor('argentinos', 65)
    elif opcion == 3:
        conversor('mexicanos', 24)
    else:
        print('Ejecuta de nuevo el programa y elige una opcion correcta.')

if __name__ == '__main__':
    # main()
    nombre = 'string largo'
    print(nombre[3:10:2])

