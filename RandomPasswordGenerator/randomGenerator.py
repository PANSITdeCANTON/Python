import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

passLen = int(input("Enter Password Lenght: "))

alphaLen = passLen//2
numLen = math.ceil(passLen*30/100)
specialLen = passLen-(alphaLen + numLen)

password = []

def generate_pass (lenght, array, is_alpha = False):
    for i in range(lenght):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0,1)
            if case == 1:
                character = character.upper()
        password.append(character)
        

generate_pass(alphaLen, alpha, True)
generate_pass(numLen, num)
generate_pass(specialLen, special)
random.shuffle(password)

gen_password = ""

for i in password:
    gen_password = gen_password + str(i)
    
print(f"Generated Password: {gen_password}")
print(f"Password: {password}")



        