"""
Materia: Seminario de Lenguaje - Python
Actividad a hacer:
Modifíque el programa anterior para que:
-Agregar las operaciones multiplicación (*) y división (/) al juego.
-Imprima al lado o debajo de cada respuesta si el resultado del usuario fué correcto o incorrecto.
-Además del tiempo informe al finalizar la cantidad de resultados correctos e incorrectos que
tuvo el usuario
"""
from random import choice, randrange
from datetime import datetime
def es_correcto(n1:int,n2:int,r:str,op:str):
    r = int(r)
    if op == '+':
        return (n1 + n2 == r)
    elif op == '-':
        return (n1 - n2 == r)
    elif op == '*':
        return (n1 * n2 == r)
    elif op == '/':
        if (n2 == 0):
            return (r == 0)
        else: 
            return (n1 // n2 == r) #La utilizacion de la division entera es para no tener que estar poniendo numeros con coma 
# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
puntos = 0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("Resultado: ")
    while not(result.isnumeric()):
            print('Porfavor ingresar un entero.')
            result = input("Resultado: ")
    if es_correcto(number_1,number_2,result,operator):
        print('Es correcto!')
        puntos+=1
    else:
        print('Es incorrecto!')
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos. Respuestas correctas: {puntos}")