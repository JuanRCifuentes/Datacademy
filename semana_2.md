#  Semana 2

- Semana 2

    - Los datos primitivos
    - Convertir un tipo de dato a un tipo diferente
    - Operadores lógicos y de comparación
    - Tu primer programa: Conversor de monedas
    - Construyendo el camino de un programa...
    - Varios paises en el conversor de monedas
    - Aprendiendo a no repetir codigo con funciones
    - Modularizando nuestro conversor de monedas
    - Trabajando con Strings
    - Strings: Slices
    - Proyecto: Palíndromo

    ## Los datos primitivos

    - Enteros

    - Floats: Números de punto flotante o decimales

        Ejemplo: `flotante = 1.5`

    - Strings: Cadenas de caracteres

        Ejemplo: `nombre = "juan"`.

        Concatenación: Se puede hacer usando el signo + ousando un f-string.

    - Booleans: Verdadero o falso

        Ejemplo: `boolean = True`.

    ## Convertir entre tipos de datos

    Existen funciones o métodos en python para cambiar entre tipos de datos. Por ejemplo, puede existir un string con valor "3", que al ser un string no permite realizar operaciones numéricas. Si escribo `"3"+ "5"` el resultado será `"35"`. Para poder relizar operaciones matematicas con este valor, se debe convertir a tipo entero. el método para convertir de strings a enteros es `int(<string_numérico>)`. 

    

    Sin embargo, esta función nos permite convertir otro tipo de objetos a entero, por ejemplo un float, al cual simplemente le quitaría su parte decimal.

    ## Operadores lógicos y de comparación

    ### Lógicos

    - `and`: Permite confirmar si todas las variables comparadas son `true`.
    - `or`: Permite confirmar si al menos una de las variables comparadas son `true`.
    - `not`: Cambia el valor de un boolean por su opuesto.

    ### Comparación

    - `==`: Permite confirmar que ambas variables son iguales
    - `!=`: Confirma que ambas variables comparadas son diferentes
    - `<`: Confirma si la primera variable es menor a la segunda variable. Tambien puede usarse en conbinación con la igualdad para tener en cuenta ambos casos `<=`.
    - `>`: Confirma que la primera variable es mayor que la segunda variable.Tambien puede usarse en conbinación con la igualdad para tener en cuenta ambos casos `>=`.

    ## Primer programa: Conversor de monedas

    Vamos a utilizar el editor de código, ya que necesitamos ejecutar muchas lineas de código y para esto la terminal no es tan práctica.

    Para aproximar al numero de decimales deseado, se utiliza el método `round()`.

    ## Condicionales

    Son utiles cuando se tienen varias opciones para continuar con la ejecucion del programa. 

    Por ejemplo, si alguien es menor de edad, se le debe prohibir la entrada a sitios para mayores de edad, de lo contrario, se le concede la entrada.

