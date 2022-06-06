
fruta='fresa'
letra=fruta[1]
print(letra)

longitud=len(fruta)
print(longitud)
ultimo=(longitud-1)
print(ultimo)


#rebanadas en strings

s= 'Monty Python'
print(s[0:5])
print(s[6:12])

f='banana'
print(f[:3])
print(f[3:])
print(f[:])


#Estring son inmutables?

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)


#operador in

var1 = 'a'
var2 = 'banana'
print(var1 in var2)


palabra = 'Pera'
if palabra < 'banana':
    print('Tu palabra,' + palabra + ', viene antes de banana')
elif palabra > 'banana':
    print('Su palabra,' + palabra + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')
    
'''
El metodo upper combierte la palabra en caracteres en MAYUSCULAS
'''
palabra1 = 'banana'
palabra_nueva1 = palabra1.upper()
print(palabra_nueva1)

'''
El metodo find busca la posicion de una cadena dentro de otra
'''
palabra2 = 'bananas'
index = palabra2.find('s')
print(index)


palabra3 = 'bananas'
print(palabra3.find('nas'))

'''
El metodo strip, elimina los espacio en blanco de una cadena
'''

linea =' Aqui vamos '
print(linea.strip())


linea2 = 'Que Tengas Un Buen Día'
print(linea2.startswith('Que'))
print(linea2.startswith('q'))


linea4 = 'Que Tengas Un Buen Dia'
print(linea4.startswith('t'))
#print(linea4.lower().startswith('q'))
print(linea4.lower()) #que tengas un buen dia


