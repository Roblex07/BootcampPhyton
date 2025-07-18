#Recorrer listas
notas =[4,5,6,6,7,8,9,6,5,6,7,8,9,8,7,6,5,4,7,4,3,4,6,7,6,6,5,5,4,10,10,10]

elementobuscar=10

#El número que yo quiero buscar es el 10

#Ejercicio 1. Tengo una lista y quiero localizar el número 10

def Buscar_1(elementobuscar, notas):
    #Precondición: se supone que la lista es correcta, en este caso es de números, y el elemento a buscar es un número
    #Poscondición: nos va a devolver un true en el caso de que el elemnto se encuentre y un false en el caso en el que no se encuentre
    
    encontrado=False
    
    #for i in range(0,len(notas)):
    #    if (notas[i]==elementobuscar):
    #        encontrado=True
    #return encontrado

    i=0
    contador = 0
    while (i<len(notas)):
        if(notas[i]==elementobuscar):
            encontrado=True
            contador = contador+1
        i=i+1
    if (encontrado==False):
        print('El elemento no ha sido encontrado')
    else:
        print('El elemnto ha sido encontrado en la lista en la posición: ', i)
        print('H sido encontrado',contador)
    return encontrado


Buscar_1(elementobuscar, notas) 