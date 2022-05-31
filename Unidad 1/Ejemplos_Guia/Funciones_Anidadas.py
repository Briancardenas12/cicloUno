

def primeraFuncion():
    print('Hola desde la funión externa ')
    
    def segundaFuncion():
        print('Hola desde la funión interna ')
        
    segundaFuncion()
primeraFuncion()


def primerNumero(x):
    def segundoNumero(y):
        return x * y
    return segundoNumero 
resultado = primerNumero(2)
print(resultado(5))



def primeraFuncion():
    x = 2
    def segundaFuncion(a):
        x = 6
        print(a + x)
    print(x)
    segundaFuncion(3)
primeraFuncion()

#El doble // es para el resultado en valor entero
#Un solo / es para el resultado en un valor decimal
y=12//3
print('El valor de de Y es: ',y)
        