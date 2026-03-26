import random
empty_dict = dict()

sides = int(input("Enter number of sides: "))
rolls = int(input("Enter number of rolls: "))
total = 0
for i in range(rolls):
    random_integer = random.randint(1, sides)
    total+=random_integer
    if random_integer in empty_dict:
        empty_dict[random_integer]+=1
    else:
        empty_dict[random_integer] =1

print(total)
