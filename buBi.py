"""
    Algoritmo de busqueda binaria: basicamente hace un barrido
    Se toma como base un valor x para la posicion en el array
    Si b > a, compara v[(a+b)/2+1 ..b] si x es menor resuelva con
    v[a.. (a+b)/2-1.. b], si x es igual, entonces ya se encontro x.
    
    Si b >= a, compara v[a] con x, si x es igual, entonces se encontro
    a, si x es diferente entonces x todavia no se encuentra.
"""

v = array()
def buBi(v, a, b, x):
    if(a >= b):
        if(v[a] == x):
            return a
        else:
            return -1
    if(v[(a+b)/2]==x):
        return (a+b)/2
    elif(v[(a+b)/2]<x):
      return buBi(v, ((a+b)/2)+1, b, x)
    else:
        return buBi(v, a, ((a+b)/2)-1, b, x)
