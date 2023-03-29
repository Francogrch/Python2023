"""
Queremos codificar una frase según el siguiente algoritmo:
    encripto("a") --> "b"
    encripto("ABC") --> "BCD"
    encripto("Rock2021") --> "Spdl3132"

"""
import string
Rot = 1 #Constante que representa la cantidad de desplazamientos

def encripto(str_men):
    retorno = ""
    for c in str_men:
        retorno = retorno + chr(ord(c)+Rot)
    return retorno
print('-'*40)
cadena = input('Ingrese cadena de caracteres: ')
print('-'*40)
var_lambda = ''.join (list(map(lambda x:chr(ord(x)+Rot),list(cadena)))) 
#Creo que quedo dificil de leer, tal vez el metodo join lo tengo que utilizar en otra linea
print('Sin lambda: ' + encripto(cadena))
print('Con lambda: '+ var_lambda)
print('-'*40)