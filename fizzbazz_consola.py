import math #para importar la libreria que encesito para los modulos
your_num = int(input('ingrese su número ')) #para tomar el valor desde la consola
def fizzbuzz(your_num):
    for num in range(1, your_num + 1):# define el rango, utilizando el valor ingresado, le suma uno por el index
        if num%3 == 0 and num%5 ==0: #para verificar primero si es divisible entre 5 y 3
            print('fizzbuzz') 
        elif num%3 == 0:
            print('fizz')
        elif num%5 ==0:
            print('buzz')
        else:
            print(num)

fizzbuzz(your_num)#define el parametro de mi funcion segun lo ingresado desde consola