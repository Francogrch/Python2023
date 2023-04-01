"""
Practica 2
Seminario de Lenguaje - Python

"""
readme = """NumPy is the fundamental package for scientific computing with Python.

- **Website:** https://www.numpy.org
- **Documentation:** https://numpy.org/doc
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/numpy/numpy
- **Contributing:** https://www.numpy.org/devdocs/dev/index.html
- **Bug reports:** https://github.com/numpy/numpy/issues
- **Report a security vulnerability:** https://tidelift.com/docs/security

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires `pytest` and `hypothesis`.  Tests can then be run after installation with:

    python -c "import numpy, sys; sys.exit(numpy.test() is False)"

Code of Conduct
----------------------

NumPy is a community-driven open source project developed by a diverse group of
[contributors](https://numpy.org/teams/). The NumPy leadership has made a strong
commitment to creating an open, inclusive, and positive community. Please read the
[NumPy Code of Conduct](https://numpy.org/code-of-conduct/) for guidance on how to interact
with others in a way that makes our community thrive.

Call for Contributions
----------------------

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions
to the source code, please contact us through the [mailing
list](https://mail.python.org/mailman/listinfo/numpy-discussion) first.

Writing code isn’t the only way to contribute to NumPy. You can also:
- review pull requests
- help us stay on top of new and old issues
- develop tutorials, presentations, and other educational materials
- maintain and improve [our website](https://github.com/numpy/numpy.org)
- develop graphic design for our brand assets and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

For more information about the ways you can contribute to NumPy, visit [our website](https://numpy.org/contribute/). 
If you’re unsure where to start or how your skills fit in, reach out! You can
ask on the mailing list or here, on GitHub, by opening a new issue or leaving a
comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to
speak to us in private first, contact our community coordinators at
numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for
an invitation).

We also have a biweekly community call, details of which are announced on the
mailing list. You are very welcome to join.

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved."""

print(f"{'Punto1':-^40}")
list_readme = readme.split("\n") 
for word in list_readme:
    if "http" in word or "https" in word:
        print(word)



print(f"{'Punto2':-^40}")
import collections
import string

list_readme = readme.lower().split() #Separamos las letras
list_words = list(filter(lambda x: x[0] in string.ascii_letters,list_readme)) #hace una lista con solo los elementos que comiencen con una letra
count_list = collections.Counter(list_words) #crea un diccionario la clave es igual a la palabra y el valor la cantidad de veces que aparece
max_word = max(count_list, key=count_list.get)
print(f"La palabra que mas aparece es: '{max_word}' . Aparecio {count_list.get(max_word)} cantidad de veces. ")



print(f"{'Punto3':-^40}")
import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones. """

"""
character = input("Ingresa una letra a buscar: ")
while not(character in string.ascii_letters):
    character = input("El valor ingresado no es una letra. Ingresa una letra: ")
jupyter_list = jupyter_info.split()
for word in jupyter_list:
    if word.lower().startswith(character.lower()):
        print(word, end=" - ")
print()
"""


print(f"{'Punto4':-^40}")
evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures."""

evaluar_list = evaluar.split('resumen:') #divido titulo de resumen
title_list = evaluar_list[0].split() #divido el titulo en palabras
title_list.pop(0) #saco la palabra titulo:
body = evaluar_list[1].split('\n') #divido de a cuerdo a  los saltos de linea del resumen
body_list = " ".join(body).split('.') #lo hago string y luego divido las oracion por puntos
body_list = body_list[:-1] #saco el ultimo elemento que es un espacio
cant_pray = {'facil': 0, 'aceptable': 0, 'dificil': 0,'muy_dificil':0} #contador de frases
for prayer in body_list:
    match len(prayer.split()):
        case lenght if lenght < 13: cant_pray['facil'] += 1 #Si no pongo el 0 me sale como el ejemplo, cosa que estaria mal ya que un espacio no es una palabra
        case lenght if 12 < lenght < 18: cant_pray['aceptable'] += 1
        case lenght if 17 < lenght < 26: cant_pray['dificil'] += 1
        case lenght if lenght > 25: cant_pray['muy_dificil'] += 1
if len(title_list) < 11:
    print('Titulo: ok')
else:
    print('Titulo: Sobre pasa las 10 palabras')
print(f"Cantidad de oraciones faciles de leer {cant_pray['facil']}, aceptables para leer: {cant_pray['aceptable']}, dificil de leer {cant_pray['dificil']}, muy dificiles de leer {cant_pray['muy_dificil']}")


"""
print(f"{'Punto 5':-^40}")
import collections
phrase = input('Ingresar frase: ')
word = input('Ingresar palabra: ')
phrase_list = phrase.lower().replace(',','').replace('.','').split()
cant = collections.Counter(phrase_list)
print(cant[word.lower()])
"""
"""
print(f"{'Punto 6 ':-^40}")
palabra = input("Ingresá una palabra: ")
if "a" in palabra and "n" in palabra:
    print("Hay letras a y n.")
else:
    print("No hay letras a y n. ")
"""
print(f"{'Punto 7':-^40}")
import string
import collections
texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

texto = texto.replace('\n',' ')
count = {'mayus':0,'minus':0,'no_letras':0}
for letter in texto:
    match letter:
        case letter if letter in string.ascii_lowercase:
            count['minus']+=1
        case letter if letter in string.ascii_uppercase:
            count['mayus']+=1
        case _:
            count['no_letras']+=1
        
texto_list = texto.lower().split()
count_text = collections.Counter(texto_list)

for elem in count_text:
    print(f"La palabra '{elem}' aparece {count_text[elem]} veces.")

"""
print(f"{'Punto 8':-^40}")

from collections import Counter
word = input("Ingrese una palabra o frase: ")
word = word.replace(" ","").lower()
word_coun = Counter(word)
word_list = list(word_coun.most_common())
print(word_list[0][1] <= 1)
"""
"""
print(f"{'Punto 9':-^40}")

points = {'A':1,'E':1,'I':1,'O':1,'U':1,'L':1,'N':1,'R':1,'S':1,'T': 1,'D':2,'G':2,'B':3,'C':3, 'M':3, 'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':20,'Z':10}
word = input("Ingresa palabra: ").upper()
sum_points = 0
for elem in word:
    sum_points += points[elem]
print(f"""#Palabra: {word}
#valor: {sum_points}""")

print(f"{'Punto 10':-^40}")
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
#Parte A
def generarDic():
    nombres_lista = nombres.replace("'","").replace(",","").split()
    alum_dic = {}
    for indice, elem in enumerate(nombres_lista):
        alum_dic[elem] = [notas_1[indice],notas_2[indice]]
    return alum_dic
#Parte B
def est_prom(alum_dic):
    alum_prom = []
    for key in alum_dic.keys():
        alum_prom[key] = (alum_dic[key][0] + alum_dic[key][1]) / 2
    return alum_prom
#Parte C
def cur_prom(alum_prom)
    prom_general = 0
    for key in alum_prom.keys():
        prom_general += alum_prom[key]
    prom_general = prom_general / len(alum_prom.keys())
    return prom_general
#Parte D
def estu_prom_max(alum_prom):
    return max(alum_prom)

#Parte E
def est_nota_min(alum_dic):
    return min(alum_dic)
