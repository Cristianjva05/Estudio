#Palíndromo
#Palíndromo es cuando una palabra le lee igual de derecha a izquierda y de izquierda a derecha 

"""
dicionario:
input
print
[::-1] = se utiliza para colocar la palabra alrevez
.remplace = lo utilio para remplazar caracteres como espacios 
.lower = lo utilio para pasar todo a minuscula , el .upper funciona para poner todo en mayuscula 

"""
print ("===============================================================")
#campo para escribir la palabra y limpia los espacios y pasar todo a minusculas
palabra = input("Escribe la palabra o frase que considera palindromo: ")
palabra = palabra.replace(" ","")
palabra = palabra.lower()
print (palabra)
#colocar la palabra de izquierda a derecha
palabrare = palabra[::-1]
print (palabrare)
#valida si la palabra alrevez es igual a la palabra normal  
if palabra == palabrare:
    print ("la palabra u oracion es palíndroma")
else:
    print ("la palabra u oracion no es palíndroma")
print ("===============================================================")
