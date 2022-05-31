def sumar_Dos_numeros():
    nun1=float(input('Ingrese el primer número: '))
    nun2=float(input('Ingrese el segundo número: '))
    #Aunque recibe un valor flotante en la operación lo convierte a entero.
    print('La suma de ', int(nun1), '+', int(nun2), 'es igual a ', int(nun1)+int(nun2))
    
def raiz_Cuadrada():
    valor = float(input('Ingrese el valor del que quiere saber la razi cuadrada: '))
    raiz= valor**0.5
    return print('El valor de la raiz cuadrada de: ', valor, 'es ', raiz)
sumar_Dos_numeros()
raiz_Cuadrada()

