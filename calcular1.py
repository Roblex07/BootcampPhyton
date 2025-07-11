#Ejericio sumar, restar, multiplicar y dividir dos numeros

#ALGORITMO
#Dos varibales que guarden la informacion de los valores de entrada
#Una variable que guarde el resultado de la operación
#Compribar que los valores introducidos por el usuraio son numeros o no
    #Si son numneros hacemos las correspondeintes operaciones
    #Si no pues print("No son numeros animal")

import numbers

def operacione(N1, N2):
    num1=N1
    num2=N2
    resultado=0
    listaresultados=[0,0,0,0,0,0]
    if isinstance(num1, numbers.Number) & isinstance(num2, numbers.Number):
        #Suma de dos valores (+)
        listaresultados[0]=num1+num2
        
        #Resta de dos valores (-)
        listaresultados[1]=num1-num2
        
        #Multiplicacion (*)
        listaresultados[2]=num1*num2
        
        #Division (/)
        listaresultados[3]=num1/num2
        
         
        for i in range (0, len(listaresultados)):
            print("El resultado de la operacion es")
            print(listaresultados[i])
    else:
        print("No son numeros animal") 
        
        
operacione(4,2)