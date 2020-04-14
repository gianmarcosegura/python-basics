# Multiplica por 2 los elementos

numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Forma PRO de hacerlo --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- Esto crea una numeva lista --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))
