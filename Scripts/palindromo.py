def main():
    palabra_original = input('Escribe una palabra: ')
    palabra_original = palabra_original.replace(' ', '')
    palabra_original = palabra_original.lower()
    palabra_invertida = palabra_original[::-1]
    if palabra_original == palabra_invertida:
        print(f'"{palabra_original.capitalize()}" es un palindromo')
    else:
        print(f'"{palabra_original.capitalize()}" NO es un palindromo')

if __name__ == '__main__':
    main()