import numbers

def fib(numero):
    a=0
    b=1
    
    if isinstance(numero, numbers.Number):
        print("es un numero")
       
        while a < numero:
                print(a, end='')
                a=b
                b=a+b
                
        print()
        print("Fin del programa")
        
    
    else:
        print("no es un numero")
    
fib(1000) 


