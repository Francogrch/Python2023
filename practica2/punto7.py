"""
7. Dada una frase identiﬁcar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de
palabras sin distinguir entre mayúsculas y minúsculas, en la frase.
"""
import string
import collections
print(f"{'Punto 7':-^40}")

text = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

text = text.replace('\n',' ')
count = {'mayus':0,'minus':0,'no_letras':0}
for letter in text:
    match letter:
        case letter if letter in string.ascii_lowercase:
            count['minus']+=1
        case letter if letter in string.ascii_uppercase:
            count['mayus']+=1
        case _:
            count['no_letras']+=1
        
text_list = text.lower().split()
count_text = collections.Counter(text_list)

for elem in count_text:
    print(f"La palabra '{elem}' aparece {count_text[elem]} veces.")
