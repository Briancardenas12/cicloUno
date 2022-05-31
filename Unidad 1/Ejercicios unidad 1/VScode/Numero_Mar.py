print('Ingrese un cuatro números diferentes')
A= int (input('Ingrse el primer numero: '))
B= int (input('Ingrse el primer numero: '))
C= int (input('Ingrse el primer numero: '))
D= int (input('Ingrse el primer numero: '))


if A>B and A>C and A>D:
    print ('El número mayor es :' + str(A))
elif B>A and B>C and B>D:
    print ('El número mayor es :' + str(B))
elif C>A and C>B and C>D:
    print ('El número mayor es :' + str(C))
elif D>A and D>B and D>C:
    print ('El número mayor es :' + str(D))
    