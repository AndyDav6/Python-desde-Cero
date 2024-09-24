'''Funcion: son bloques de codigo reutilizables que 
realizan una tarea especifica'''

'''Definicion de una funcion: una funcion se define usando la 
palabra clave "def", seguida del nombre de la funcion, 
parentesis () y dos puntos :. El codigo dentro de la funcion 
debe estar indentado'''

'''Parametros de la funcion: los parametros son valores que puedes 
pasar a una funcion. Se colocan entre parentesis en la definicion
de la funcion'''

'''Llamada a una funcion: para usar una funcion. debes llamarla.
Esto se hace escribiendo el nombre de la funcion seguido de 
parentesis () y proporcionando cualquier parametro necesario'''

#1 Funcion predefinida
print("Me llamo Andy Namaja")

#2 Funcion predefinida len() --> el "len" calcula la longitud de la lista.
mi_lista = [1, 2, 3, 4]
longitud = len(mi_lista)
print(longitud)

#3 Funciones definidas por el  usuario
def sumar (a, b):
    return a + b
resultado = sumar(15, 4)
print(resultado)

#4 Funciones con argumentos por defecto
def saludar(nombre = "bro"):
    print(f"Hola, {nombre}")

saludar()
saludar("Dan")

#5 Funciones anonimas (lambda)
multiplicar = lambda x, y: x * y
print(multiplicar(5,3))

#6 Funciones con numeros variables de argumentos
''' *args: permite pasar un numero variable de argumento no nombrados'''
def sumar_todos(*args):
    return sum(args)
print(sumar_todos(3, 6, 9 ,12))

''' **kwargs: permite pasar un numero variable de argumentos con nombre'''
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_info(Nombre="Gaby", Edad="20", Ciudad="Cuenca")

#7 Funciones recursivas
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#8 Defincion de una funcion simple
def saludar():
    print("Hola, her doctor")
saludar()

#9 Definicion de una funcion con parametros
def saludo_peresonalizado (nombre):
    return(f"¡Hola, {nombre}!")
saludo_peresonalizado("David")

#10 Definicion de una funcion que retorna un valor
def suma(c, d):
    return c + d
resultados = suma(13, 45)
print(resultados)

#11 Definicion de una funcion con valores por defecto
def saludos(nombre = "mundo"):
    print(f"¡Hola, {nombre}!")
saludos()
saludos("David")

#12 Definicion de una funcion corta
doblar = lambda x: x * 2
print(doblar(7))

#14 Definicion de una funcion con multiples retornos
def operaciones(e, f):
    sumas = e + f
    resta = e - f
    return sumas, resta

resultado_suma, resultado_resta = operaciones(93, 5)
print(resultado_suma)
print(resultado_resta)

"""Función sin parámetros: Define una función llamada imprimir_mensaje que imprima el mensaje “¡Aprendiendo Python!”. """
"""Función con parámetros: Define una función llamada suma que tome dos números como parámetros y devuelva su suma."""
"""Llamada a funciones: Llama a las funciones imprimir_mensaje y suma con los parámetros adecuados."""