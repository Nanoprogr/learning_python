#usaremos in para recorrer y buscar los valores deseados
#iniciamos con string, cambia el valor de word para ahcer q se contenga o no en sentence
sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'quics'

if word in sentence:
    print('the word was found')
else:
    print('the word was not found')

#para buscar en una lista, cambia el valor de value para que se content¡ga o no en la lista

num = [1, 2, 3, 4, 5]

value = 9

if value in num:
    print(f'the value {value} is on the list')
else:
    print(f'the value {value} is not on the list')