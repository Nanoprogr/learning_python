"""crearemos una funcion fizzbuzz"""
def fizzbuzz(your_num):
    """definiendo la funcion fizzbuzz"""
    for num in range(1, your_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)

console_num = int(input('Ingrese su número '))#toma el valor desde la consola

fizzbuzz(console_num)#define el parametro de la funcion desde el valor ingresado en la consola
