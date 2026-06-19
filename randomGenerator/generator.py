import random
import string 

all = string.ascii_letters + string.digits + string.punctuation

lenght = 16 

password = "".join(random.choices(all, k=lenght))

print(f"Password: {password}")