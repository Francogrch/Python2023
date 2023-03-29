
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
nombre = 'Lionel'
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
lista.sort() #ordena lista
sorted(lista, key=str.lower) #ordena, considerando a todos los str como lower
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

#CONJUNTOS
#Coleccion heterogenea, desordenada, valores unicos, no idexada
set(("Soda Stéreo", "La Renga"))
set('alabanza') # {'a', 'b', 'l', 'z', 'n'}
bandas = {"AC/DC", "Metallica", "Greta Van Fleet", "Soda Stéreo", "Los Piojos"}
for elem in bandas: #recorrer
    print(elem)
"""
Operaciones matemáticas sobre conjuntos:
    in: retonar si un elemento pertenece o no a un conjunto.
    |: unión entre dos conjuntos.
    &: intersección entre dos conjuntos.
    -: diferencia de conjuntos
"""
bandas = {"AC/DC", "Metallica", "Greta Van Fleet", "Soda Stéreo", "Los Piojos"}
bandas_nacionales = set(("Soda Stéreo", "La Renga", "Los Piojos"))
print("Los Piojos" in bandas) # True
todos = bandas | bandas_nacionales
en_ambos = bandas & bandas_nacionales
internacionales = bandas - bandas_nacionales
bandas.add("Foo Fighters") #Agregar
bandas.issubset() # boolean es un subconjunto de otro conjunto
bandas.isdisjoint() # disjuntos
bandas.issuperset() # es un superconjunto de otro conjunto
bandas.update() #Agrega elementos de un conjunto
bandas.discard("Soda Stéreo")  #Borra elemento si existe
bandas.remove("Foo Fighters") #Trata de borrar elemento, si no existe da error



#funciones
def funcion(parametros):
    """ Aca va el docstring """
    sentencias
    return <expresion> #Puede no ir el return

    return cant_aeo, cant_iu, len(cadena) #devuelve una tupla
#parametros
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

#Variables locales y globales
def prueba():
    y = 1
    def prueba_2():
        nonlocal y #para poder acceder a la variable anterior a la funcion
        y = 11
        return 1
    
    global x #para acceder a variable global
    x = 3
    
#Espacio de nombres
"""Cuando se invoca a una función, se crea un espacio de nombres local con todos los recursos
definidos en la función y que se elimina cuando la función finaliza su ejecución.
"""


"""...
Simple es mejor que complejo.
...
Plano es mejor que anidado.
...
Espaciado es mejor que denso.
La legibilidad es importante.
..."""

#Atributos de funciones
funcion.__doc__ #es el docstring**.
funcion.__name__ # es una cadena con el nombre la función.
funcion.__defaults__# una tupla con los valores por defecto de los parámetros


#Lambda - Funciones anonimas
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
map(funcion, lista) #aplica una funcion en cada elemento de la lista, y retorna una estructura de datos tipo map
#filter
filter(funcion,lista) #aplica funcion en cada elemento de la lista, y retorna una estructura con los valores que cumpla la condicion