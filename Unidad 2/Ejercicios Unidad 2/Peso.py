print('Codigo para calcular el peso de Lb a Kg')
constante_K=0.453592
constante_L=1
pesoL= float(input('Ingrese el valor del peso en libras: '))

resultado_K=((pesoL*constante_K)/constante_L)

print(f"La conversión del {pesoL} en libras en kilogramos es de: {resultado_K}")
