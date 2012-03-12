"""
    Algoritmo para calcular el maximo de un arreglo con los supuestos:
    si a < b v[a..(a+b)/2] y v[(a+b)/2 + 1 .. b] resolviendo por recursividad
    si a = b el maximo seria v[a]
    Luego comparar cual es mayor y lo devuelve
"""
v = array()
def maxnum(v , a, b):
    maxim1, maxim2 = 0
    if (a < b):
        maxim1 = maxnum(v, a, (a+b)/2)
        maxim2 = maxnum(v, ((a+b)/2)+1, b)
        if(maxim1 > maxim2):
            return maxim1
        else:
            return maxim2
    else:
        return v[a]
     
    
    
    
