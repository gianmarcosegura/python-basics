# Strings

# En este caso el segundo print sigue imprimiendo Pedro
name = 'Pedro'

saludo = f'Hola, {name}'

print(saludo)

name = 'Paco'

print(saludo)

saludo2 = 'Hola, {}'
con_format = saludo2.format(name)

print(con_format)

saludo3 = 'Hola {}, que tal en {}'
con_format3 = saludo3.format('Manolo', 'Madrid')

print(con_format3)
