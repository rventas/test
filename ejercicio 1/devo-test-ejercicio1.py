def clasificar_numero(n):
    suma = sum([i for i in range(1,n) if n%i == 0])
    if (suma == n):
        return 'perfecto'
    elif (suma > n):
        return 'abundante'
    else:
        return 'defectivo' 
def clasificacion(lista):    
    return [{i:clasificar_numero(i)} for i in lista]
