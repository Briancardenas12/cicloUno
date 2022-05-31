import math
print('Programa para calcular la hipotenusa de un triangulo')

a= float(input('Ingrese el valor del primer lado: '))
b= float(input('Ingrese el valor del segundo lado: '))

c= math.sqrt((a**2) + (b**2))

print(f"El resultado de la hipotenisa con lado a: {a} y lado b: {b} es: {c}")
