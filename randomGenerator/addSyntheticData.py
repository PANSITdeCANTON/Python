import random

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"
allCharacters = alpha + num + special

arrayLen = int(input("Enter Array Lenght: "))
initialArray = input("Enter Initial Array Units: ")

array = list(initialArray)

if len(array) < arrayLen:
    needChars = arrayLen - len(array)
    print(f"Adding Synthetic Data in the Array. Generating {needChars} Synthetic Data's")
    
    for _ in range(needChars):
        char = random.choice(allCharacters)
        
        if char in alpha:
            if random.choice([True, False]):
                char = char.upper()
        array.append(char)
elif len(array) > arrayLen:
    array = array[:arrayLen]

random.shuffle(array)

gen_array = ""

for i in array:
    gen_array += str(i)
    
print("\nFinal Array:")
print(array)
print(f"Final Length: {len(array)}")
print(f"Randomized Array: {gen_array}")


        