print('Codigo para saber si un número es primo')
Num= int(input('Ingrese un numero entero positivo: '))

for i in range(2, Num):
    #print(i)
    modul= Num%i 
    #print(modul)
    if modul == 0:
        print(i)
    
    