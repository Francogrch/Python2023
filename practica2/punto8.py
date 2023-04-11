"""
8. Escriba un programa que solicite que se ingrese una palabra o frase y permita identiﬁcar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma es
una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
"""
print(f"{'Punto 8':-^40}")

from collections import Counter
import string
word = input("Ingrese una palabra o frase: ")
word = "".join(list(filter(lambda character: character in string.ascii_letters,word)))#armo una list con solo los caracteres que sean letras, y luego los hago un string
word = word.replace(" ","").lower()

word_coun = Counter(word)
word_list = list(word_coun.most_common())
if word_list[0][1] <= 1:
    print('Es un heterograma')
else:
    print('No es un heterograma')
    
