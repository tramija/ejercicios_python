#FUNCIONES SIN PARAMETROS
"""
def bienvenida():
    print('Bienvenda a python')
    
    return
bienvenida()

def bienvenida(nombre):
    print('Bienvenidad apython', nombre + '!')
    return

bienvenida('Diana')


def bienvenda(nombre, apellido):
    print('Binevenidad a python', nombre, apellido +'!')
    
    return
bienvenda('Diana', 'Jaramillo')

"""

"""

def derechos_humanos():
    print('Derecho a la vida')
    print('Derecho a la educacion')
    print('Derecho a la recrecion')
    
    
derechos_humanos()



def derechos_mayor_edad():
    print('Derecho votar')
    print('Derecho al trabajo')
    print('Derecho a una vivienda')
    
derechos_mayor_edad()

#fUCIONES CON PARAMETROS 

def mayoria_edad(nombre, edad):
    print(f'Segùn la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayor_edad()
        
    else: 
        derechos_humanos()
        
        
mayoria_edad('diana', 40)
mayoria_edad('albert', 13)


#Funciones con parametros opcionales 

def mayoria_edad2(edad, nombre='X'):
    print(f'Segùn la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayor_edad()
        
    else: 
        derechos_humanos()
        
        
            
mayoria_edad2(40)


def suma(a, b):
    result =a +b
    print(result)
    return result


suma(2, 5)


def operaciones(a, b):
    suma = a+b
    multiplicacion = a*b
    resta = a-b
    div = a/b
    
    
    return suma, multiplicacion, resta, div


s, m, r, d =operaciones(4, 6)

print(s,m, r, d)

def menu(*platos):
    print('Hoy tenemos:', end='')
    for plato in platos:
        print(plato, end=', ')
        return
    
platos = menu('ensalada', 'arroz')
print(platos)
"""


# Ordnamiento burbuja 

def ordenamiento_burbuja(lista):
    for n in range(len(lista)-1, 0, -1):
        for i in range(n):
            if lista[i]> lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1]= temp
                
numeros = [100, 60, 78, 9, 0, 34, 67, 12, 1]
print(numeros)


ordenamiento_burbuja(numeros)
print(numeros)


#Ordenamiento por seleccion


def ordenamiento_seleccion(lista):
    for n in range(len(lista) -1, 0, -1):
        posicion_maxima = 0
        
        for l in range(1, n + 1):
            if lista[l] > lista[posicion_maxima]:
                posicion_maxima = l
                
        temp = lista[n]
        lista[n] = lista[posicion_maxima]
        lista[posicion_maxima] = temp
        
        
               
numeros = [100, 60, 78, 9, 0, 34, 67, 12, 1]
print(numeros)


ordenamiento_seleccion(numeros)
print(numeros)



