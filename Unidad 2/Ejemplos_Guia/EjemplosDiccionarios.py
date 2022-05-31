def promeioNotas(nota1, nota2, nota3, nota4):
    promedio= round((nota1 + nota2 + nota3 + nota4)/4, 2)
    return promedio

print (promeioNotas(3.0,2.1,5.0,4.7))


'''
Se crea un diccionario vacio y se comienza a agregar las keys and values
luego se toman los values y se operan
'''
def promedioNotas2(dict):
    sumatoria=0
    sumatoria+=dict["nota1"]
    sumatoria+=dict["nota2"]
    sumatoria+=dict["nota3"]
    sumatoria+=dict["nota4"]
    
    promedio=round(sumatoria/4,2)
    return promedio


dicNotas ={'nota1':3.0, 'nota2':2.1, 'nota3':5.0, 'nota4':4.7}

#dicNotas ['nota1']=3.0
#dicNotas ['nota2']=2.1
#dicNotas ['nota3']=5.0
#dicNotas ['nota4']=4.7

print(promedioNotas2(dicNotas))