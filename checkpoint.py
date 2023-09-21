# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.
import math

def ListaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    list_numbers_divisibles = [];
    if tope < numero: return list_numbers_divisibles;
    
    for nDisisible in range(tope + 1):
        if (not (numero + nDisisible) % numero and numero + nDisisible <= tope):
            list_numbers_divisibles.append(numero + nDisisible)
    
    return list_numbers_divisibles;

def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    if exponente == 0: return 1;
    if exponente == 1 : return numero;
    if exponente > 1 :
        expo = 1
        res = numero
        while expo < exponente:
            res *= numero
            expo += 1
    
    if math.floor(exponente) != exponente: # if is decimal expot
        res = pow(numero, exponente)
    
    if exponente < 0 : # exponente negative
        exponente *= -1 # if is negative change positive
        num = 1 / numero 
        res = Exponente(num, exponente);
    
    return res;

def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    if type(lista) is not list: return None
    # algoritmo recursive
    result = [] # list matrix data values
    
    for i in range(len(lista)): 
        if (type(lista[i]) is list): # de matrix a array add
            result.extend(ListaDeListas(lista[i]))
            continue
        result.append(lista[i])
    
    return result

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    if not numero: return 1
    return numero * Factorial(numero - 1)

def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    if not (type(desde) is int and type(hasta) is int) : return None;
    # range n primos recurvive algoritmo
    
    def rangePrimos(nPrimo, nMaxPrimo = 0, data = []):
        result = [];
        isPrimo = True;
        
        i = 2;
        while nPrimo > i and i < nPrimo: # calculate is primo range, > 2 and < nPrimo - 1
            if not nPrimo % i:
                isPrimo = False;
                break;
            i += 1; 

        if (nPrimo == 1 or nPrimo > 1) and isPrimo : result.append(nPrimo)
        if (nPrimo < nMaxPrimo): result.extend(rangePrimos(nPrimo + 1, nMaxPrimo, []));
        return result;
    
    return rangePrimos(desde, hasta);

def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
    '''
    result = [];
    if type(lista) is not list: return None; 
    if not len(lista): return result;

    for i in range(len(lista) - 1):
        first_value = lista[i]
        count_values = 1
        serach = False
        
        if (len(result)): 
            for ifind in range(len(result)):
                if first_value == result[ifind][0]: serach = True
        if not serach:
            for j in range(len(lista) - (i + 1)):
                if first_value == lista[i + (j + 1)]: count_values += 1

            result.append((first_value, count_values));
    
    return result

def ClaseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:
        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    y debe tener el siguiente método:
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    class ClaseVehículo() :
        
        def __init__(self, tipo, color):
            self.tipo = tipo
            self.color = color
            self.velocidad = 0
            
        def Acelerar(self, inc):
            self.velocidad = max(0, min(self.velocidad + inc, 100)) 
            return self.velocidad
            
    return ClaseVehículo(tipo, color)

def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    if not (type(diccionario_par) is dict): return None;
    if not (clave in diccionario_par) : return None;
    
    # descendente < mayor a menor, ascendente menor a mayor
    result = {}
    
    def list_sorted (list_sorted, descendente=True):
        for i in range(len(list_sorted)):
            for j in range(len(list_sorted) - 1):
                if (descendente == True and list_sorted[j] > list_sorted[j + 1]) or (descendente == False and list_sorted[j] < list_sorted[j + 1]):
                    temp = list_sorted[j]
                    list_sorted[j] = list_sorted[j + 1]
                    list_sorted[j + 1] = temp
        
        return list_sorted
    
    def getValuesKeyOrder(list_order, f_clave): # lorder : ['a','b','c'], clave2
        list_key_values = []
        
        for i in range(len(list_order)): 
            list_clave_default = diccionario_par[clave]
            list_clave = diccionario_par[f_clave]

            index = list_clave_default.index(list_order[i]) # 1
            list_key_values.append(list_clave[index])
        
        return list_key_values
    
    def getSortedkeys(result):
        res = {}
        sorted_list = sorted(result);
        for i in range(len(sorted_list)):
            res[sorted_list[i]] = result[sorted_list[i]]
        
        return res
    
    result[clave] = list_sorted(diccionario_par[clave].copy(), descendente)
    for key in diccionario_par:
        if key != clave: 
            result[key] = getValuesKeyOrder(result[clave], key)
    
    #sort clave dict
    return getSortedkeys(result) 