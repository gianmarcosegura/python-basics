l = ['uno', 'dos', 'tres'] # List == Array
t = ('uno', 'dos', 'tres') # Tuples, no se pueden modificar, agregar ni eliminar elementos  
s = {'uno', 'dos', 'tres'} # Sets, se agrega elementos con .add, no tienen un orden, no pueden tener elementos duplicados

l.append('cuatro')
s.add('cuatro')

print(l)