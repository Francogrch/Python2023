
#CADENAS
cadena = "Python"
string_1 = 'Python' 
string_2 = "ATENCION" # 'ATENCION'
string_3 ="""Hola
        Texto de varias lineas
            """
string_1 + string_2 #PythonATENCION
string_1 * 4 #PythonPythonPythonPython
len(string_1) #Longitud de cadena 6
cadena[-2]
cadena[3:] #El formato es cadena[inicio:fin]
cadena[:]
#Las cadenas son INMUTABLES.

#Metodos de cadenas
cad = "Holaaa"
cad.upper() #HOLAAA
cad.lower() #holaaa
cad.islower() #False
cad.isupper() #False
cad.count("a") #3
cad.center(70, "*") #'*******************Holaaa********************'
cadena.startswith("2")
cadena.endswith(("ar", "er", "ir"))
cad.strip() # Elimina todos los caracteres que esten como parametros
cadena.startswith("2") #bool si comienza con ese valor
cadena.endswith(("ar", "er", "ir")) #bool si comienza con esos valores. Se pasa una tupla
"Somos campeones del mundo!!!".split() #['Somos', 'campeones', 'del', 'mundo!!!']
cad = "Hola {} !! Intentaste {} "
cad.format('Lionel', 4 ) #Definir una cadena con cierto formato predefinido
'Hola Lionel !! Intentaste 4'



#OPERADOR IN
if "a" in cad: # operador in para saber si existe el caracter
    print("Hay letras a")

#MODULO STRING
import string
minusculas = string.ascii_lowercase # 'abcdef...z'
mayusculas = string.ascii_uppercase# 'ABCDEF...Z'
digitos = string.digits #'0123456789'

#FOR
cadena = "0123"
for elem in cadena:
    print(elem)

#Funcion Range() devuelve secuencia de numeros enteros
valor_inicial = 1
valor_final = 10
paso = 1
range(valor_inicial,valor_final,paso) # '1,2,3,4,5,6,7,8,9,10'
range(valor_final) # '0,1,2,3,4,5,6,7,8,9'


#print
#f-String
nombre = Lionel
intento = 4
print(f'Hola {nombre} !! Intestaste {intento}')
'Hola Lionel !! Intentaste 4'

print(f"La mejor canción de todas:\n{cad1:<30}\n{cad2:>50}") 
print(f"\n{cad3:^30}") 
print(f"\n{cad4:*^50}")
#\n salto de linea
#cad1:<30 Justifica izquierda
#cad2:>50 Justifica derecha
#cad3:^30 Centra
#cad4:*^50 Centra con caracter *

for i in range(10):
    print(i, end="-") #Cambia \n por '-'
#0-1-2-3-4-5-6-7-8-9-

#Expresion condicional
 A if C else B #Devuelve A si se cumple C, si no devuelve B

#Python evalua con circuito corto
#LISTAS
lista = [] #son mutables
varios = [1, "dos", [3, "cuatro"], True] #Heteregeneas
varios[2][1] = [3, "cuatro"]
#Metodos
lista.append(x) #agrega atras
sum(list) #suma de los elementos(numeros) de la lista
len(list) #cantidad de elemntos
lista2 = []
lista2 = lista.copy() #Copiar para no hacer referencia a la misma
duracion_pelis = [152, 161, 142, 157, 138, 153, 146, 130]
promedio = sum(duracion_pelis) / len(duracion_pelis)
mayor_prom = [n for n in duracion_pelis if n > promedio]


#Tuplas INMUTABLES
tupla = ()
tuplas_1 = (1,) #sin el , no es una tupla


#Diccionario 
dic = {} #diccionario vacio
dic = {'clave': 'valor', 'clave1':'valor'} #Claves unicas e inmutables
dic.keys() #lista con llaves
dic.values() #lista con valores
dic.items() #lista con claves y valores

dict([(n, ord(n)) for n in string.digits])#Constructor