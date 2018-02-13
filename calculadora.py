#!/usr/bin/python3

#Álvaro López García

import sys

def sum (op1,op2):
    return op1 + op2
def resta (op1,op2):
    return op1 - op2
def mult (op1,op2):
    return op1 * op2
def div (op1,op2):
    try:
        return op1 / op2
    except ZeroDivisionError:
        return("No se puede dividir entre 0")

funciones = {"suma":sum,"resta":resta,"multiplicacion":mult,"division":div}

if __name__=="__main__":

    try:
        operador = sys.argv[1]
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except IndexError:
        sys.exit("usage : [operador][num1][num2]")
    except ValueError:
        sys.exit("El argumento 2 y 3 tienen que ser tipos numericos")

    try:
        resultado = funciones[operador](num1,num2)
        print(resultado)
    except KeyError:
        sys.exit("Tienes que usar un operador matematico como: suma, resta, multiplicacion o division")

       
