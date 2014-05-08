#!/src/bin/python

import math
from sympy import *

def factorial(numero):
  factorial = 1
  while(numero > 1):
    factorial = factorial * numero
    numero = numero - 1
  return factorial
  
def derivada(x, numero, centro):
  c = Symbol('c')
  f = sin(c)
  suma = f.evalf(subs={c: centro})
  for i in range (1,numero + 1):
    f_i = diff(f, c)
    v = f_i.evalf(subs={c: centro})
    s= (v / factorial(i)) * ((x - centro) ** i)
    suma = suma + s
    f = f_i
  print suma
  return derivada

def suma_taylor(x, numero, centro):
  for i in range (1, numero+1):
    derivada(x, i, centro)      
  
  return suma_taylor
    
  
