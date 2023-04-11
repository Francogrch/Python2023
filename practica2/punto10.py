"""
10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
A. Generar una estructura todas las notas sin que se repitan, sin guardar los nombres de los
estudiantes.
B. Calcular el promedio de notas de cada estudiante.
C. Calcular el promedio general del curso.
D. Identiﬁcar al estudiante con la nota promedio más alta.
E. Identiﬁcar al estudiante con la nota más baja.
"""
print(f"{'Punto 10':-^40}")

#Parte A
def parteA(notas_1,notas_2):
    """ Esta funcion genera una lista sin elementos repetidos, con dos listas pasadas por parametros
    """
    return (list(set(notas_1 + notas_2)))
#Parte B
def est_prom(alum_dic):
    """ Esta funcion genera un diccionario con nombres como llaves y con el promedio de las dos notas como valor.
    Recibe como parametro:
    -un diccionario con strings como llaves, y como valor una lista con dos enteros.
    """
    alum_prom = {}
    for key in alum_dic.keys():
        alum_prom[key] = (alum_dic[key][0] + alum_dic[key][1]) / 2
    return alum_prom
#Parte C
def cur_prom(alum_prom):
    """ Esta funcion retorna el promedio general de de los valores de un diccionario. Recibe como parametro un 
    diccionario con valores de tipo enteros.
    """
    prom_general = 0
    for key in alum_prom.keys():
        prom_general += alum_prom[key]
    prom_general = prom_general / len(alum_prom.keys())
    return prom_general
#Parte D
def estu_prom_max(alum_prom):
    """Esta funcion retorna la llave con el maximo valor en un diccionario, recibe como parametro un diccionario
    con valores de tipo enteros.
    """
    return max(alum_prom)

#Parte E
def est_nota_min(alum_dic):
    """Esta funcion retorna la llave con el minimo valor en un diccionario
    """
    return min(alum_dic)

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#Parte A
print(f"{'Parte A':-^40}")
con_notas = parteA(notas_1,notas_2)
for elem in con_notas:
    print(elem)

#Parte B
print(f"{'Parte B':-^40}")
notas = zip(notas_1,notas_2)
nombres = nombres.replace(',','').replace("'",'')
nombres = nombres.split()
dic_alum = dict(zip(nombres,notas))
prom_alum = est_prom(dic_alum)
print('Promedio de cada estudiante')
for key in prom_alum.keys():
    print(f'{key} = {prom_alum[key]}')

#Parte C
print(f"{'Parte C':-^40}")
promedio = cur_prom(prom_alum)
print(f'Promedio del curso {promedio:.2f}')

#Parte D
print(f"{'Parte D':-^40}")
nota_alta = estu_prom_max(prom_alum)
print(f'El estudiante con la nota promedio mas alta es {nota_alta}.')

#Parte E
print(f"{'Parte E':-^40}")
nota_baja = est_nota_min(dic_alum)
print(f'El estudiante con la nota mas baja es {nota_baja}.')