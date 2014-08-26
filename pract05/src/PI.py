#!/usr/bin/python

n = int(raw_input('Introduzca el valor de n: '))

suma = 0.0
for i in range(1,n+1):
  x_i=(i-0.5)/float(n)
  fx_i=4/(1+x_i*x_i)
  
  suma=suma+fx_i

PI_i=suma/float(n)



print 'Aproximacion de PI es: ', PI_i
