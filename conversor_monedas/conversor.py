def main():
    dinero_pesos = float(input('Cuanto dinero tienes en pesos colombianos? '))
    tasa_pesos_dolares = 1/4100
    dinero_dolares = dinero_pesos * tasa_pesos_dolares
    print(f'You have {round(dinero_dolares, 2)} US {"Dollar" if dinero_dolares==1 else "Dollars"}')

if __name__ == '__main__':
    main()
