"""Python resumen teoria
...
Simple es mejor que complejo.
...
Plano es mejor que anidado.
...
Espaciado es mejor que denso.
...
La legibilidad es importante.
"""
#----------------------------------------------------Tipos de datos
#Cadenas
#Las cadenas son INMUTABLES.
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

#Metodos de cadenas
cad = "Holaaa"
cad.upper() #HOLAAA
cad.lower() #holaaa
cad.islower() #False
cad.isupper() #False
cad.count("a") #3
cad.center(70, "*") #'*******************Holaaa********************'
cad.strip() # Elimina todos los caracteres que esten como parametros
cadena.startswith("2") #bool si comienza con ese valor
cadena.endswith(("ar", "er", "ir")) #bool si comienza con esos valores. Se pasa una tupla
"Somos campeones del mundo!!!".split() #['Somos', 'campeones', 'del', 'mundo!!!']
cad = "Hola {} !! Intentaste {} "
cad.format('Lionel', 4 ) #Definir una cadena con cierto formato predefinido
'Hola Lionel !! Intentaste 4'

#f-String
nombre = 'Lionel'
intento = 4
print(f'Hola {nombre} !! Intestaste {intento}') # 'Hola Lionel !! Intentaste 4'
print(f"La mejor canción de todas:\n{nombre:<30}\n{intento:>50}")  #\n salto de linea, nombre:<30 Justifica izquierda, intento:>50 Justifica derecha
print(f"{nombre=}") #nombre = 'Lionel'
print(f"\n{nombre:^30}") #:^30 Centra
print(f"\n{intento:*^50}") #*^50 Centra con caracter *


#----------------------------------------------------Estructuras de control y usos
#Expresion condicional
 A if C else B #Devuelve A si se cumple C, si no devuelve B
#Python evalua con circuito corto

#OPERADOR IN
if "a" in cad: # operador in para saber si existe el caracter
    print("Hay letras a")

#FOR
cadena = "0123"
for elem in cadena:
    print(elem)
for i in range(10):
    print(i, end="-") #Cambia \n por '-' retorna 0-1-2-3-4-5-6-7-8-9-

#Funcion Range() devuelve secuencia de numeros enteros
valor_inicial = 1
valor_final = 10
paso = 1
range(valor_inicial,valor_final,paso) # '1,2,3,4,5,6,7,8,9,10'
range(valor_final) # '0,1,2,3,4,5,6,7,8,9'

#----------------------------------------------------Estructuras de datos (Colecciones)
#Listas
lista = [] #son mutables
varios = [1, "dos", [3, "cuatro"], True] #Heteregeneas
varios[2][1] = [3, "cuatro"]
lista2 = lista.copy() #Copiar para no hacer referencia a la misma
duracion_pelis = [152, 161, 142, 157, 138, 153, 146, 130]
promedio = sum(duracion_pelis) / len(duracion_pelis)
#List Comprehension (Teoria de Conjuntos)
mayor_prom = [n for n in duracion_pelis if n > promedio] # n por cada n en duracion_peli si n es mas grande que promedio
enzos = [jugador for jugador in jugadores_por_pais.values() for jugadomayor_prom = [n for n in duracion_pelis if n > promedio]r in jugadores if "Enzo" in jugador]
#Metodos
lista.append(x) #agrega atras
lista.sort() #ordena lista

sorted(lista, key=str.lower) #ordena, considerando a todos los str como lower
list(reversed(lista)) #retorna lista al revez
sum(list) #suma de los elementos(numeros) de la lista
len(list) #cantidad de elemntos
max(duracion_pelis) #retorna el numero maximo de la coleccion
min(duracion_pelis) #retorna el minimo de la coleccion

#Tuplas (INMUTABLES - No se agrega/modificar ni eliminan)
tupla = ()
tuplas_1 = (1,) #sin el , no es una tupla
nombre_y_apellido = ("Fernando", "Lopez")
nombre_y_apellido = tuple(["Fernando", "Lopez"])
nombre_y_apellido[1] #'Fernando'


#Diccionarios
dic = {} #diccionario vacio
dict([(n, ord(n)) for n in string.digits]) #Constructor recibe iterable
dic = {'clave0': 'valor', 'clave1':20} #Claves unicas e inmutables
#Metodos
dic.keys() #lista con llaves
dic.values() #lista con valores
dic.items() #lista con claves y valores
for clave, valor in dic.items(): #recorrer diccionario con variables
    print(f"{clave} : {valor}")


#Conjuntos
#Coleccion heterogenea, desordenada, valores unicos, no idexada
#Acceso rapido y eficiente para saber si un elemnto esta en el conjunto
set('alabanza') # {'a', 'b', 'l', 'z', 'n'}
bandas_nacionales = set(("Soda Stéreo", "La Renga", "Los Piojos")) #constructor
bandas = {"AC/DC", "Metallica", "Greta Van Fleet", "Soda Stéreo", "Los Piojos"}
#Set Comprehension
mayor_prom_set = {n for n in duracion_pelis if n > promedio}

#Operaciones
for elem in bandas: #recorrer
    print(elem)    
print("Los Piojos" in bandas) # retorna si el elemento esta en el conjunto
todos = bandas | bandas_nacionales #unión entre dos conjuntos.
en_ambos = bandas & bandas_nacionales #intersección entre dos conjuntos.
internacionales = bandas - bandas_nacionales # diferencia de conjuntos
bandas.add("Foo Fighters") #Agregar
bandas.issubset() # boolean es un subconjunto de otro conjunto
bandas.isdisjoint() # boolean si son disjuntos
bandas.issuperset() # boolean si es un superconjunto de otro conjunto
bandas.update() #Agrega elementos de un conjunto
bandas.discard("Soda Stéreo")  #Borra elemento si existe
bandas.remove("Foo Fighters") #Trata de borrar elemento, si no existe da error

#----------------------------------------------------Funciones
def funcion(parametros):
    """ Aca va el docstring """
    sentencias
    return <expresion> #Puede no ir el return

    return cant_aeo, cant_iu, len(cadena) #devuelve una tupla con todas las variables
#--------parametros
def mi_musica(dicci_musica, tipo_musica="internacional", nombre="lisa"): #los que tienen valores por defecto siempre van al final de la lista de parámetros
    return None

#Usar los argumentos indefinidos como listas
def imprimo(*args): #puede ir cualquier nombre
    """ Esta función imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")

#Usar los argumentos indefinidos como diccionarios
def imprimo_otros_valores(**kwargs): #puede ir cualquier nombre
    """ ..... """
    for clave, valor in kwargs.items():
        print(f"{clave} es {valor}")
secuencia = (1, 2, 3)

#Pasar argumento como diccionario
secuencia = (1, 2, 3) #En este caso paso 3 valores y no 1 lista.
imprimo(*secuencia)

#Pasar Diccionario como diccionario
contacto = {"nombre": "Messi", "celu": 12345}#En este caso paso 2 claves y 2 valores, no 1 diccionario.
imprimo_otros_valores(**contacto)

#Atributos de funciones
funcion.__doc__ #es el docstring**.
funcion.__name__ # es una cadena con el nombre la función.
funcion.__defaults__# una tupla con los valores por defecto de los parámetros

#--------Lambda - Funciones anonimas
lambda parametros : expresion

lista_de_acciones = [lambda x: x * 2, lambda x: x * 3]
for accion in lista_de_acciones:
    print(accion(2))

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(2)
print(f(42))
print(make_incrementor(22)(33))

#map
list(map(funcion, lista)) #aplica una funcion en cada elemento de la lista, y retorna una estructura de datos tipo map
num_por_dos = list(map(lambda x: x * 2,range(10)))#retorna los numeros de 0 a 9 multiplicados por 2

#filter
list(filter(funcion,lista)) #aplica funcion en cada elemento de la lista, y retorna una estructura con los valores que cumpla la condicion
num_div_5 = list(filter(lambda x: x % 5 == 0,range(100)))#retorna los numeros que sean divisivles por 5 de 0 a 99



#zip 
list(zip(lista1,lista2,lista3))#itera al mismo tiempo en varias colecciones retorna una estructura con los valores en los mismos indices unidos
#enumerate
list(enumerate())#asocia un numero a cada iteracion, retorna tuplas con el numero de iteracion, y el valor
#Variables locales y globales
def espacio_de_nombres():
    """ Hay tres espacio de nombres, que se crean en diferentes momentos y tienen diferente tiempo de vida:
        - __builtins__: se crea al iniciar el interprete y nunca se elimina
        - Globales: se crea en la definicion de un modulo y normalmente tambien dura hasta que el interprete finaliza
        - Locales: se crean al invocar una funcion es llamada y se elimina cuando la funcion retorna    
    """
    y = 1
    def prueba_2():
        nonlocal y #para poder acceder a la variable anterior a la funcion
        y = 11
        return 1
    
    global x #para acceder a variable global
    x = 3

#---------------------------------------------Modulos
import nombreModulo #Con esto podemos acceder a las funciones y variables del modulo(archivo)
#Actualiza espacios de nombres
#__pycache__ .pyc carga mas rapido en memoria, ya que esta copilado
import nombreModulo import * # (No recomendable) importa todas las funciones del modulo y no es necesario llamarlas por el nombre de los modulos
import nombreModulo as m #iguala el nombre del modulo con m
m.recurso #uso de recuro en la variable m(nombreModulo)
import carpeta.nom_carpeta.nom_subdirectorio #Para buscar en una direccion especifica se cambian los / por .
import importlib
importlib.reload(modulo) #Recarga el modulo ya que los modulos se cargan en cada sesion del intermprete

dir(modulo) # Retorna lista ordenada con los nombres definidos

import builtins
dir(builtins) #retorna lista ordenada con nombres predefinidos

#Modulos 

import collections #Este modulo tiene mas estructuras de datos que las definidas por el lenguaje
cant_letras = collections.Counter('asxfgf')
print(cant_letras.most_common(1)) #retorna la letra mas comun
d = collections.deque('xxcvdf') #pilas y colas

import sys
#sys.exit() #sale del programa actual
sys.path #Lista de cadenas donde cada cadena son los directorios donde busca los modulos
sys.platform #Retorna sistema operativo

import string
minusculas = string.ascii_lowercase # 'abcdef...z'
mayusculas = string.ascii_uppercase# 'ABCDEF...Z'
digitos = string.digits #'0123456789'

#__init__.py si este archivo esta en la carpeta, python interpreta el directorio como un paquete
__all__ = ["echo","surround"] #esta variable puede estar en __init__.py, y si importamos todo de un packete que contiene mas paquetes, solo va a importar los modulos que esten en esta lista

from functools import reduce
#reduce
list(reduce(funcion,lista)) #aplica funcion con varias variables y un resultado, retorna la operacion en un iterable
list(reduce(lambda a, b: a + b, sumar(10)))


#NUevas lineas

#---------------------------------------------------------------------Archivos 
if __name__ == "__main__": #Sirve para que se ejecute automaticamente
    import sys
    uno(sys.argv[1]) #argv[0] = nombre del archivo; argv[1] = parametro escrito por consola
open(nombreArchivo)#crea la asignacion dentro del programa con el archivo y en modo 'r'
open(nombre,modo)
modo = {'r':'read','w':'write','a':'append','x':'create'} # 'r'(escritura) y 'w'(escritura) pone el puntero al principio mientras que el 'a' al final. 'x' da error si ek archivo existe
# puede tener un + o un b ademas de las claves del diccionario. con + agrega permisos de lectura/escritura y con b significa que es binario
arch = open('archivo.txt','w') #Crea archivo.txt para escritura en la misma carpeta del script
# FileExistError si ya esta creado
import locale
locale.getLocale()#Saber codificaion, encoding

import os
ruta = os.path.dirname(os.path.realpath(".")) #ruta actual del archivo
ruta_completa = os.path.join(ruta,"carp1","carp2","archivo.txt")#genera una ruta con las carpetas aniadidas

#Almacenar datos en un archivo
f = open("archivo.txt",'w')
f.write('En Argentina naci') #Agrega el string al archivo y retorna la cantidad de caracteres que pudo guardar
f.read(x)#lee el archivo siendo x la cantidad de veces que se mueve el puntero
f.close() #cierra el archivo
if f.read() == "":
    print('Esta en EOF')
f.readlines()#retorna lineas
for linea in f: #leer lineas
    print(linea)
#JSON Forma de intercambio de datos
import json
diccionario = {"equipo": "Bestia", "esport": "CSGO", "pais": "Argentina"}
lista_de_dic = [{"equipo": "Bestia", "esport": "CSGO", "pais": "Argentina"}, {"equipo": "equipo2", "esport": "CSGO", "pais": "Argentina"}]
json.dumps(lista_de_dic, indent=4)#Devuelve string
json.dump(lista_de_dics,archivo)#de Python a JSOn . guarda lista de dic en formato JSON en archivo
loads()#de JSON a formato Python para string
lista_de_dic = json.load(archivo) #convierte JSON a Python. Y guarda el diccionario o lista en la varible 
#Datasets
#formato CSV
#Comma Separated Value
import csv
csvreader = csv.reader(archivo,delimiter = ',') #genera un objeto iterador, y el delimiter es el archivo que separa los datos
encabezado = next(csvreader)
for linea in csvreader:
    if linea[1] == "Movie":
        print(f"{linea[2]:<40 {linea[3]}}")
show_ar = filter(lambda x:x[5] == "argentina" and x[1] == "Movie", csvreader)

csvreader = csv.DictReader(archivo, delimiter='-') #genera Diccionario

archivo_csv_ = open("bandas.csv","w")
writer = csv.writer(archivo_csv)
writer.writerow(['Colum1','Colum2']) #Escribe fila

#with
with open("bandas.csv") as archcsv:
    csv_reader = csv.reader(archcv, delimiter=',')

#cierra automaticamente el archivo
#Desafio