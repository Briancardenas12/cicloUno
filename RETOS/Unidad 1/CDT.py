def CDT(usuario:str, capital:int, tiempo:int):
    porcentaje_interes=0.03
    porcentaje_perder=0.02
        
    if tiempo>=3:
        valor_interes=(capital*porcentaje_interes*tiempo)/12
        Valor_total=(valor_interes+capital)
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {Valor_total}")

    elif tiempo <=2:
        valor_perder=(capital*porcentaje_perder)
        Valor_total=(capital-valor_perder)
        return(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {Valor_total}")
        
print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366', 650000, 2))
   

