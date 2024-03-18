def fizzbuzz(your_num):
    for num in range(1, your_num + 1):#define rango, suma 1 para incluir valor ingresado
        if num%3 == 0 and num%5 ==0: #para verificar primero si es divisible entre 5 y 3
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 ==0:
            print('Buzz')
        else:
            print(num)
fizzbuzz(100)