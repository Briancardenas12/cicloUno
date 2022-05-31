from multiprocessing.spawn import import_main_path
import numpy
import math
print('CALCULO DE FIGURAS GEOMETRICAS')

def superficie_triangulo(Base:int, Altura:int):
    
    superficie=(Base*Altura)/2
    #print(superficie)
    return superficie

def area_circulo(R:int):
    y=numpy.pi
    Area=y*(R**2)
    return Area

def base_triangulo(superficie:int,altura:int):
    base=(superficie*2)/altura
    return base

def radio_circulo(area:int):
    radio=(area/numpy.pi)
    radio_1=math.sqrt(radio)
    return radio_1


print('SELECCIONE UNA OPCION')
print('1. Superficie del triangulo')
print('2. Area de un circulo')
print('3.Base de un triangulo')
print('4.Radio de un circulo')

x=int(input('Ingrese una opción: '))

if x ==1:
    D1=int(input('Ingrese el valor de la base:'))
    D2=int(input('Ingrese el valor de la altura: '))
    Resultado_Area_T=superficie_triangulo(D1, D2)
    print(Resultado_Area_T)

elif x==2:
    D3=int(input('Ingrese el valor del radio: '))
    Resultado_Area_C=area_circulo(D3)
    print(Resultado_Area_C)
    
elif x==3:
    D4=int(input('Ingrese el valor de la superficie: '))
    D5=int(input('Ingrese el valor de la altura: '))
    
    Resultado_Base=base_triangulo(D4, D5)
    print(Resultado_Base)
    
elif x==4:
    D6=int(input('Ingrese el valor del área del circulo: '))
    Resultado_radio=radio_circulo(D6)
    print(Resultado_radio)
    
    
    
    
    
    
     