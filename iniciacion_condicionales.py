# cambia el valor de age para que se ajuste a cada condicion y se imprima el str necesario
age = 15

if age < 25:
    print('sorry, you nedd to be at least 25 y.o. to reant a car')
elif age > 100:
    print(f'sorry, {age} is too ald to rent a car')
else:
    print('ok, you can rent a car')