#Consigue la @
data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion = data.find('@')
print(enlaposicion)
#Consigue el espacio luego de uct.ac.za
espacioenlaposicion = data.find(' ',enlaposicion)
print(espacioenlaposicion)
#Corta el fragmento localizado previamente
host = data[enlaposicion+1:espacioenlaposicion]
print(host)


# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
cadena3 = "Hola\nMundo"
print(cadena3)
# Saldrá una única línea en pantalla y la \ y la n será visibles como caracteres normales.
cadena2 = r"Hola\nMundo"
print(cadena2)


cadena = "un uno, un dos, un tres"
print (cadena.count("un")) # Saca 4, hay 4 "un" en cadena.
print (cadena.count("un",10)) # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
print (cadena.count("un",0,10)) # Saca 3, hay 3 "un" entre la posición 0 y la 10



cadena4 = "un uno, un dos, un tres"
print (cadena4.replace("un", "XXX"))
print (cadena4.replace("un", "XXX", 2))
# saca por pantalla "XXX XXXo, XXX dos, XXX tres"
# Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"