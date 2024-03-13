import psycopg2

# runs query to get all students
# and prints all students
def getAllStudents():
    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

# runs query to insert a new student
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES('" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "')")
    conn.commit()

# runs query to update a students email
def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = '" + new_email + "' WHERE student_id = " + student_id + ";")
    conn.commit()

# runs a query to delete a student
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = " + student_id + ";")
    conn.commit()

# connects to db
conn = psycopg2.connect(host="localhost", dbname="school", user="postgres", password="postgres", port=5432)

cur = conn.cursor()

# loops asking user which function to run till they exit
while True:

    # printing choices for user
    print("1: getAllStudents()")
    print("2: addStudent(first_name, last_name, email, enrollment_date)")
    print("3: updateStudentEmail(student_id, new_email)")
    print("4: deleteStudent(student_id)")
    print("5: exit program")

    choice = input("enter number:")

    #if statments for each choice
    if choice == "1":
        getAllStudents()
    if choice == "2":
        #asking user for inputs
        first_name = input("enter first_name:")
        last_name = input("enter last_name:")
        email = input("enter email:")
        enrollment_date = input("enter enrollment_date (yyyy-mm-dd):")
        addStudent(first_name, last_name, email, enrollment_date)
    if choice == "3":
        #asking user for inputs
        student_id = input("enter student_id:")
        new_email = input("enter new_email:")
        updateStudentEmail(student_id, new_email)
    if choice == "4":
        #asking user for input
        student_id = input("enter student_id:")
        deleteStudent(student_id)
    if choice == "5":
        print("exiting")
        break

conn.commit()

cur.close()
conn.close()

