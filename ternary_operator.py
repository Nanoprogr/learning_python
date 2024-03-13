#ternary operator, iniciemos con la sintaxis normal (cambia el rol para imprimir segun condicion)
rol = 'admin'

if rol == 'admin':
    auth = 'can access'
else:
    auth = 'can not access'

print(auth)

#ternary operator, une todo en una linea (cambia el rol para imprimir segun condicion)

rol_dos = 'admin'
auth_dos = 'can access' if rol_dos == 'admin' else 'can not access'

print(auth_dos)