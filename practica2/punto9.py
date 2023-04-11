"""
9. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la
siguiente tabla de valores del juego Scrabble:

A, E, I, O, U, L, N, R, S, T  = 1
D, G = 2
B, C, M, P = 3
F, H, V, W, Y = 4
K = 5
J, X = 8
Q, Z = 10
"""
import string
print(f"{'Punto 9':-^40}")

points = {'A':1,'E':1,'I':1,'O':1,'U':1,'L':1,'N':1,'R':1,'S':1,'T': 1,'D':2,'G':2,'B':3,'C':3, 'M':3, 'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':20,'Z':10}
word = input("Ingresa palabra: ").upper()
error = False
sum_points = 0
for elem in word:
    if (elem in string.digits):
        print('No ingresaste una palabra')
        error = True
    else:
        sum_points += points[elem]
if not(error):
    print(f"""#Palabra: {word}
#valor: {sum_points}""")
