"""
3. Dado el siguiente texto guardado en la varible jupyter_info, solicite por teclado una letra e imprima
las palabras que comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique el error.
"""
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

character = input("Ingresa una letra a buscar: ")
print(len(character))
while  (len(character) > 1) or not(character in string.ascii_letters):
    character = input("El valor ingresado no es una letra. Ingresa una letra: ")
jupyter_list = jupyter_info.split()
for word in jupyter_list:
    if word.lower().startswith(character.lower()):
        print(word, end=" - ")
print()