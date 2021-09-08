class Parrot:

    # klases atribúti
    species = "bird"

    # objekta atribúti
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Parrot klases objektu izveidosana
firstParrot = Parrot("Blu", 10)
secondParrot = Parrot("Woo", 15)

# izsauc Parrot klases objektu klases atribútus
print("Blu is a {}".format(firstParrot.__class__.species))
print("Woo is also a {}".format(secondParrot.__class__.species))

# izsauc Parrot klases objektu atribútus
print("{} is {} years old".format(firstParrot.name,firstParrot.age))
print("{} is {} years old".format(secondParrot.name,secondParrot.age))