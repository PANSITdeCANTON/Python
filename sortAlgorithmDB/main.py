import random
from faker import Faker
# Import the functions from your connect.py file
from connect import read_employees, write_employee

fake = Faker()

def generate_and_save_fake_employees(count=100):
    print(f"Generating {count} mock employees...")
    education_options = ["High School", "Bachelor's", "Master's", "PhD"]
    
    for _ in range(count):
        # 1. Determine Gender & Name
        sex = random.choice(["M", "F"])
        name = fake.name_male() if sex == "M" else fake.name_female()
        
        # 2. Generate plausible metrics safely
        age = random.randint(18, 65)
        
        # FIX: Ensure max experience cannot drop below 0 if age is less than 22
        max_xp = max(0, age - 22)  
        xp = random.randint(0, max_xp)  
        
        education = random.choice(education_options)
        rating = round(random.uniform(1.0, 5.0), 1)
        dept_id = random.randint(1, 5)      # Matches your SSMS department keys
        
        # 3. Write directly to SSMS using your imported function
        write_employee(name, age, sex, xp, education, rating, dept_id)

if __name__ == "__main__":
    # You updated the function parameter default to 100, 
    # but you are passing 5 here. Change this to 100 if you want 100 records!
     while True:
        more = input("Press (Enter) to inject more, (q) to quit")
        if more == "q":
            break
        generate_and_save_fake_employees(100)
    
        print("\n--- Fetching updated database tables ---")
    # Step 2: Read the database back to confirm it worked
        read_employees()