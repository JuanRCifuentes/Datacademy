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

    Otro caso de elegir el comportamiento de un programa, es el que se presenta en el convertidor de monedas (archivo `conversor.py`), en el cual basado en una eleccion del usuario, se puden utilizar diferentes tipos de monedas para convertir.

    ## Funciones: No repetir codigo

    La misma logica a veces se escribe varias veces, sin embargo, pude darse nombre a unos pasos especificos y ejecutarlos juntos con solo escribir su nombre.

    Este nombre que agrupa varios pasos se le llama "funcion". Para definir una funcion en python se utiliza la siguiente sintaxis:

    ```python
    def nombre_funcion(<parametros>):
        paso_1
        paso_2
        return    
    ```

    `return`: Este comando es para enviar alguna variable afuera de la funcion, especificamente a donde la estan llamando. Lo que se ponga luego del return statement, sera lo que representara a la funcion en donde se le este utilizando. SIN EMBARGO, si no se escribe nada leugo del return statement, se termina en ese punto la ejecucion de la funcion.

    Los parametros son los valores que se envian a la funcion para que esta pueda ejeutar su codigo.

    Las funciones sirven para "Modularizar" el codigo.

    ## Cadenas de caracteres
    Existen metodos especificos para los strings que ayudan a su manipulacion. Ejemplos de estos son:
    1. `upper()`: Pone en mayusculas todas las letras del string.
    2. `capitalize()`: Pone en mayuscula la primera letra del string.
    3. `strip()`: Ayuda a quitar los espacios al principio o al final de un string.
    4. `lower()`: Cambia todas las letras del string a minusculas.
    5. `replace(a, b)`: Cambia todas las letras a por las letras b.

    Muchos de estos metodos no hacen cambios al string original, simplemente retornan un nuevo string con los cambios. Esto quiere decir que si queremos "arreglar" algun string, se debe actualizar su valor:
    ```python
    nombre = 'juan'
    juan = nombre.capitalize()
    ```

    Los strings en python, son como listas de caracteres (como su nombre lo dice). Eso significa que podemos hacer uso de un indice para acceder a los caracteres que los componen. Tambien se puede usar con un string la funcion len(), que retorna la cantidad de caracteres que tiene el string.

    ### Rebanadas (Slices)
    Los strings (al igual que otro tipo de listas), se puden rebanar. Esto significa que puedo tomar partes especificas con un inicio o un final definido dentro del string original. esto se hace con la siguiente sintaxis: `string[a:b:c]`, en donde a es el indice del primer elemento que quiero, b es el indice del elemento que quiero y c es un numero que representa los saltos que quiero tener en cuenta a la hora de obtener los elementos del string original. 
    
    Por ejemplo: 
    ```python
    nombre = 'string largo'
    nombre[3:10:2]
    ```
    Va a retornar:
    ```shell
    iglr
    ```

    El ultimo elemento se puede representar con -1, y si se quiere ir de atras para adelante en el string, se puede escribir -1 en el tercer numero.

    ## Palindromo
    Un palindromo es una palabra o frase que se lee igual al invertirse el orden de sus letras. Ejemplos: 
    1. 'Luz azul'
    2. 'Ana'

    En el archivo `palindromo.py` se encuentra nuestra funcion que dice si una palabra es un palindromo o no.