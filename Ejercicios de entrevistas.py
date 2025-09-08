"""
Ejercicios de entrevistas

1.Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

2.Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

3.Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

4.Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

5.Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

6.Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.

7.Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

8.Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

9.Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

 """

#1.Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
print ("===============================================================")
print( "Este programa busca tomar dos numero y traerme el numero mayor")
def mimax (a, b):#def es para crer mi propia función , el cual indico que tome dos numero   
    #la funcion es lo mismo de max solo que mio jeje
    if a>b:#aqui realizo un if para saber si el numero A es mayo a B
        return a# si es el casi trae A
    else:
        return b#si no b


NUMERO1 = int (input ("Escribe el primer numero: "))#pido el numero A
NUMERO2 = int (input ("Escribe el segundo numero: "))#pido el numero B
numeromayor = mimax (NUMERO1,NUMERO2) # ejecuto la formula q cree
print ("el numero mayor es ", numeromayor) #resultado
print ("===============================================================")

#2.Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def mimax2 (a,b,c):
    if a>b:
        return a
    else :
        if b>c:
            return b
        else:
            return c 
        
numeroo1= int (input ("dijite numero"))
numeroo2= int (input ("dijite numero"))
numeroo3= int (input ("dijite numero"))

numeromayor3 = mimax2 (numeroo1,numeroo2,numeroo3)
print (numeromayor3)
 

print ("===============================================================")

#3.Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

caracter =  (input ("Escribe una vocal: "))
caracter = caracter.lower()
print (caracter)

vocales = ["a","e","i","o","u"]

for mapa in vocales:
    if mapa == caracter:
        print ("true")
