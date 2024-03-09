import mysql.connector

def ranks():
# Connect to the MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shivamdave@12345678",
        database="VIT_university_db",
    )

    # Create a cursor object
    cursor = conn.cursor()


    retrieve_rank_query = """
        SELECT s.name, s.usn, m.Crypto, m.SWE, m.Java, m.OOPS, m.Python
        FROM students s
        JOIN marks m ON s.usn = m.usn
    """

    cursor.execute(retrieve_rank_query)
    result = cursor.fetchall()

    # Process and save the results to files
    count=0
    for row in result:
        name, usn, java, python, crypto, swe, oops = row
        sum=java + python + crypto + swe + oops
        total_marks=(java + python + crypto + swe + oops) 
        if total_marks > 300:
            rank = "Good"
        elif 175 <= total_marks < 300:
            rank = "Average"
        else:
            rank = "Need Improvement"
        
        
        if rank=="Need Improvement":
            count=count+1
            print(count)
        # Create a file with usn.txt and write the report
            with open(f"{usn}.txt", "w") as file:
                file.write(f"Name: {name}, USN: {usn}\n")
                file.write(f"Crypto: {crypto}\n")
                file.write(f"SWE: {swe}\n")
                file.write(f"OOPS: {oops}\n")
                file.write(f"Python: {python}\n")
                file.write(f"Java: {java}\n")
                file.write(f"Total: {sum}\n")
                file.write(f"rank: {rank}")

# Close the connection
    conn.close()

def rank():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivamdave@12345678",
    database="vit_university_db",
    )

    # Create a cursor object
    cursor = conn.cursor()


    retrieve_rank_query = """
        SELECT  m.Crypto + m.SWE + m.OOPS + m.Java + m.Python as total_marks
        FROM students s
        JOIN marks m ON s.usn = m.usn
    """

    cursor.execute(retrieve_rank_query)
    result = cursor.fetchall()

    ranks_stud=[]

    for row in result:
        total_marks=row[0]
        if int(total_marks) > 300:
            rank = "Good"
        elif 175 <= int(total_marks) < 300:
            rank = "Average"
        else:
            rank = "Need Improvement"
        ranks_stud.append(rank)
        
    return ranks_stud


ranks()
