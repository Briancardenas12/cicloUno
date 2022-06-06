def doblar(numero):
    return numero*2

numero=[2,3,4,5,6,7,8,9,10]

print(list(map(doblar, numero)))
print(list(map(lambda x: x*2, numero)))