# Diferencia
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)
print(local_friends)


# Suma
local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends_total = local.union(abroad)
print(friends_total)


# Coincidencia
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)
