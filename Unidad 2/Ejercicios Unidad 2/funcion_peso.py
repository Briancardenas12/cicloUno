def peso_c(peso_L:float): # Se defie la funcióncon un argumento
    constante_K=0.453592 #Se definen las dos constantes
    constante_L=1
    
    resultado_K=((peso_L*constante_K)/constante_L) #Operación regla de 3 para hacer la conversión, guardado en una variable
    return(f"El valor del peso {peso_L} en libras convertido en a kilogramos es: {resultado_K}") #Se retorna un str 
    
D1=float(input('Ingrese el valor del peso en libras: ')) #Se solicia ingresar el valor por teclado

print(peso_c(D1)) #Se llama la función y se imprime lo que hay en el retorno




    
    
    
    