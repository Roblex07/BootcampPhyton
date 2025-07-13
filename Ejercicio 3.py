num=input('Introduce el número: ')
dividendo=2
import numbers
try:
    isinstance(float(num), numbers.Number)
    resultado=float(num)
    if resultado % dividendo == 0:
        print('Es par')
    else:
        print('No es par')
    
except ValueError:
    print('Eso no es un número')

    