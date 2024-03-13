''' en este caso utilizaremos los compound conditional
    < , >, =, ¡=, entre otros, en este ejercicio
    nos piden hacer una funcion que evalue number si esta entre
    1 y 100 (inclusive) que arroje Success y si no Failure
'''

number = 101

def compound_conditional(number):
    if 1 <= number <=100:
        print("Success!")
    else:
        print("Failure...")

compound_conditional(number)