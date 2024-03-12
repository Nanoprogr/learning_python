#para importar math que me ayuda con el redondeo y el sqrt
import math 

# para importar decimal que me ayuda con los valores decimales
from decimal import Decimal

#crear mi lita
my_list = [1, 19, 3, 4, 5, 23, 7, 8, 59, 10]
print(my_list, type(my_list))

#crear mi tupple
my_tupple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tupple, type(my_tupple))

#crear mi float
my_float = 1.1
print(my_float, type(my_float))

#crear mi integer
my_integer = 1
print(my_integer, type(my_integer))

#crear mi decimal
my_decimal = Decimal(1.1)
print(my_decimal, type(my_decimal))

#crear mi diccionario
my_dictionary = {
  "casa" : 4,
  "arbol" : 5,
  "automovil" : 9
}
print(my_dictionary, type(my_dictionary))

#redondear mi float hacia arriba
my_float_up = math.ceil(my_float)
print(my_float_up, type(my_float_up))

#obtener la raiz cuadrada de mi float
my_float_sqrt = math.sqrt(my_float)
print(my_float_sqrt, type(my_float_sqrt))

#obtener el primer elemnto de mi diccionario
"""para tomar el elemnto completo utilizo .items convirtiendolo en lista
   metiendolo en una variable, y luego imprimo la variable
   esto me da el elemento sin tener que saber sy key o value"""
felement_mydict = list(my_dictionary.items())[0]
print(felement_mydict)

#para obtener el segundo elemnto de mi tupple
my_sec_tup = my_tupple[1]
print(my_sec_tup)

#para agregar un elemento al final de mi lista
my_list += [6]
print(my_list)

#para agregar un elemento con el metodo append
my_list.append(7)
print(my_list)

#para agregar un lemento al final de la lista con extend
my_list.extend([200]) 
print(my_list)

#para reemplazar el primer elemento de mi lista
my_list[0] = 0
print(my_list)

#para ordernar alfabeticamente mi lista
my_list.sort()
print(my_list)

#reasignar tupple para agregar un elemnto 
my_tupple += ('este es mi nuevo elemento',)
print(my_tupple)
