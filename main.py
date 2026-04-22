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

for num in range(1,sides+1):
    if num in empty_dict:
        p = empty_dict[num]/rolls
        print(f"Frequency: {num} -> {empty_dict[num]} -> {p:.2f}")
        
    else:
        print(f"Frequency: {num} -> 0 -> 0.0")

print(f"{total/rolls:.3f}")
