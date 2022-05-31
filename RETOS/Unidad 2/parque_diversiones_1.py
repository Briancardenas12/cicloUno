import random
def cliente(informacion:dict):
    if (informacion['edad']>18):
        atraccion= 'X-Treme'
        apto=True
        if (informacion['primer_ingreso']==True):
            total_boleta=(20000*0.95)
        else:
            total_boleta=20000
    elif(informacion['edad']>=15 and informacion['edad']<=18):
        atraccion='Carros chocones'
        apto=True
        if(informacion['primer_ingreso']==True):
            total_boleta=(5000*0.93)
        else:
            total_boleta=5000
    elif(informacion['edad']>=7 and informacion['edad']<15):
        atraccion='Sillas voladoras'
        apto=True
        if(informacion['primer_ingreso']==True):
            total_boleta=(10000*0.95)
        else:
            total_boleta=10000
    else:
        apto=False
        atraccion='N/A'
        total_boleta='N/A'        
    resultado={'nombre':informacion['nombre'], 'edad':informacion['edad'],'atraccion':atraccion,'apto':apto, 'primer_ingreso':informacion['primer_ingreso'], 'total_boleta':total_boleta}   
    return (resultado)

id_cliente=1
nombre='Johana Fernandez'
edad=random.randrange(21)
primer_ingreso= random.randrange(2)
inf={'id_cliente':id_cliente, 'nombre':nombre,'edad':edad,'primer_ingreso':primer_ingreso}
print(cliente(inf))





