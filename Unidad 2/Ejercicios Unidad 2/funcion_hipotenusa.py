import math
def hipotenusa(a:float, b:float):
    
    c= math.sqrt((a**2) + (b**2))
    return(f"El resultado de la hipotenisa con lado a: {a} y lado b: {b} es: {c}")

a= float(input('Ingrese el valor del primer lado: '))
b= float(input('Ingrese el valor del segundo lado: '))

print(hipotenusa(a, b))