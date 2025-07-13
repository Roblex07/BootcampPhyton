color=input('Introduce un color: ')
color=color.lower
if color=="verde":
    print('Usted puede pasar sin problema')
elif color=="amarillo":
    print('Usted puede pasar con dificultades')
elif color=="rojo":
    print('Usted no puede pasar bajo ningún concepto')
else:
    print('Color no reconocido')