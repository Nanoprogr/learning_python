#el proceso normal
num_list = range(1, 11)
cube_num = []

for num in num_list:
    cube_num.append(num ** 3)

print(cube_num)
print(list(num_list))

#comprehension method
num_list_dos = range(1, 11)
cube_list_dos = [num ** 3 for num in num_list_dos]
print(cube_list_dos)
print(list(num_list_dos))

#comprehension method with conditional

num_list_tres = range(1, 11)
cube_list_tres = [num ** 3 for num in num_list_tres if num % 2 == 0]
'''[] para que sea una lista, elevar num al cubo, para cada num en num_list_tres, 
si el modulo a dos es cero (para que sea par)'''
print(cube_list_tres)
print(list(num_list_tres))