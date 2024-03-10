import mysql.connector
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ranks import ranks,rank
from auto_mailing import send_email
import subprocess
import time
# Function to generate random email addresses
def generate_email(usn, domain):
    return f"{usn.lower()}.{domain}"

# Function to generate random names
def generate_name():
    first_names = ["Lionel", "Cristiano", "Helen", "Karishma", "Anushka", "Virat", "Asap", "Arpit", "Frank", "Taylor"]
    last_names = ["Messi", "Ronaldo", "Keller", "Khanna", "Rathod", "Kohli", "Rocky", "Bala", "Ocean", "Swift"]

    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivamdave@12345678",
    database="vit_university_db",
)

# Create a cursor object
cursor = conn.cursor()

students = [] 
marks_data = []  

for i in range(61, 72):
    usn = f"1nt21cs{i:03d}"
    name = generate_name()
    semester = 5
    student_email = generate_email(usn, "vit.student.ac.in")
    # print(type(student_email))
    # student_email="1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in","1nt21cs198.venkatesh@nmit.ac.in"
    # student_email = ",".join(student_email)    
    parents_email = f"parent{i}@gmail.com"

    students.append((usn, name, semester, parents_email, student_email))

    # Generate random marks for each subject (assuming out of 100)
    marks = [random.randint(20,50 ) for _ in range(5)]
    marks_data.append((usn, *marks))  # Use a different variable for marks data

# Insert data into the 'students' table
insert_student_query = "INSERT INTO students (usn, name, semester, parents_email, student_email) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(insert_student_query, students)

# Insert data into the 'marks' table
insert_marks_query = "INSERT INTO marks (usn, Crypto, SWE, OOPS , Java, Python) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_marks_query, marks_data)  # Use the correct variable

# Commit the changes and close the connection
conn.commit()
conn.close()

ranks()

rankos=rank()
for r in rankos:
    if r == "Need Improvement":
        send_email("Invitation to Performance Review Session", "Dear Student , \n I hope this email finds you well. As part of our commitment to your academic success, we would like to invite you to a personalized performance review session to discuss your progress and address any concerns or questions you may have \n Follow the link given below (http://172.18.239.190:8501) \n Ps. This is an automated mail.", "asad.aziz2021@vitstudent.ac.in")


command = "streamlit run C:/Users/Shivam Dave/Desktop/Student-Guidance/chatbot_utils/main.py"

subprocess.run(command,shell=True)



