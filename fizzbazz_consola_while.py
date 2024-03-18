def fizzbuzz(your_num):
    for num in range(1, your_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz') 
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)

while True:
    console_num = int(input('Ingrese su número o escriba 0 para salir: '))

    if console_num == 0:
        print('Fin de la función')
        break

    fizzbuzz(console_num)
