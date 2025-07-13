#Ejericio sumar, restar, multiplicar y dividir dos numeros

#ALGORITMO
#Dos varibales que guarden la informacion de los valores de entrada
#Una variable que guarde el resultado de la operación
#Comprobar que los valores introducidos por el usuraio son números o no
    #Si son números hacemos las correspondientes operaciones
    #Si no pues print("No son numeros animal")

import numbers
num1=input('Número 1: ')
num2=input('Número 2: ')
listaresultados=[0,0,0,0,0,0]
if isinstance(float(num1), numbers.Number) & isinstance(float(num2), numbers.Number):
    #Suma de dos valores (+)
    listaresultados[0]=float(num1)+float(num2)
    
        #Resta de dos valores (-)
    listaresultados[1]=float(num1)-float(num2)
        
        #Multiplicacion (*)
    listaresultados[2]=float(num1)*float(num2)
        
        #Division (/)
    listaresultados[3]=float(num1)/float(num2)
        
         
    for i in range (0, len(listaresultados)):
        print("El resultado de la operacion es")
        print(listaresultados[i])
else:
    print("No son numeros animal") 
        
        
        