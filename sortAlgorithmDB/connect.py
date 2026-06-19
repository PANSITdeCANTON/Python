from dbConnection import get_connection

def read_employees():
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    
    # Your exact SELECT query
    query = """
    SELECT TOP (1000) [EmployeeId]
          ,[Name]
          ,[Age]
          ,[Sex]
          ,[YearsOfExperience]
          ,[EducationLevel]
          ,[Rating]
          ,[DepartmentId]
      FROM [employeeAnalyticsDb].[dbo].[Employee]
    """
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        print("--- Employee Records ---")
        for row in rows:
            print(f"ID: {row.EmployeeId} | Name: {row.Name} | Age: {row.Age} | Rating: {row.Rating}")
            
    except Exception as e:
        print("Failed to read data:", e)
    finally:
        conn.close()

def write_employee(name, age, sex, xp, education, rating, dept_id):
    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor()
    
    # Insert query (EmployeeId is usually an Identity/auto-increment column, so we omit it)
    query = """
    INSERT INTO [dbo].[Employee] ([Name], [Age], [Sex], [YearsOfExperience], [EducationLevel], [Rating], [DepartmentId])
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    
    try:
        cursor.execute(query, (name, age, sex, xp, education, rating, dept_id))
        conn.commit()  # CRITICAL: Always commit changes when writing/inserting data
        print(f"Successfully added employee: {name}")
    except Exception as e:
        print("Failed to write data:", e)
    finally:
        conn.close()
        
def get_employee_ratings():
    """
    NEW FUNCTION: Safely extracts all ratings from the database 
    and returns them as a clean list of decimal/float values.
    """
    conn = get_connection()
    if not conn:
        return []

    cursor = conn.cursor()
    
    # We filter out NULL values to prevent sorting algorithms from crashing
    query = """
    SELECT [Rating] 
    FROM [employeeAnalyticsDb].[dbo].[Employee] 
    WHERE [Rating] IS NOT NULL
    """
    
    try:
        cursor.execute(query)
        # Pulls the first element of each database row and casts it as a Python float
        ratings = [float(row[0]) for row in cursor.fetchall()]
        return ratings
    except Exception as e:
        print("Failed to extract ratings:", e)
        return []
    finally:
        conn.close()
