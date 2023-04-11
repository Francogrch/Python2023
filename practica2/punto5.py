"""
5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, y
sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir entre
mayúsculas y minúsculas.
"""
print(f"{'Punto 5':-^40}")
import collections
phrase = input('Para la frase: ')
word = input('Palabra: ')
phrase_list = phrase.lower().replace(',','').replace('.','').split()
cant = collections.Counter(phrase_list)
print('Resultado ' + str(cant[word.lower()]))
