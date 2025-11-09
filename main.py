# main.py
# for 4 required functions in demo

import psycopg2
from datetime import date

# info
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "studentsdb"
DB_USER = "postgres"
DB_PASS = "li4165651234"

def connect():
    """Create and return a DB connection!"""
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )

def getAllStudents():
    """
    READ: Retrieve + Print all rows frmo student table
    getAllStudents() requirement
    """
    with connect() as conn:
        # using cursor to run SQL cmds
        with conn.cursor() as cur:
            cur.execute("""
                SELECT student_id, first_name, last_name, email, enrollment_date
                FROM public.students
                ORDER BY student_id;
            """)
            rows = cur.fetchall()
            if not rows:
                print("(no rows)")
            else:
                for r in rows:
                    print(r)

def addStudent(first_name, last_name, email, enrollment_date):
    """
    CREATE: Insert a student row, ignore if email already exists.
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO public.students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
            """, (first_name, last_name, email, enrollment_date))
        conn.commit()
    print("[ADD] Tried to add", email, "(ignored if duplicate)")


def updateStudentEmail(student_id, new_email):
    """Updates the email address for the specified student_id w/ primary key"""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE public.students
                SET email = %s
                WHERE student_id = %s;
            """, (new_email, student_id))
        conn.commit()
    print("Updated:", student_id, "->", new_email)

def deleteStudent(student_id):
    """DELETE: Deletes the record of the student with the specified student_id"""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM public.students WHERE student_id = %s;", (student_id,))
        conn.commit()
    print("Deleted:", student_id)

# demo for video 
if __name__ == "__main__":
    print("Initial:")
    getAllStudents()

    # INSERT demo, adds one new student
    addStudent("Alice", "Li", "alice.li@gmail.com", date(2023, 9, 3))

    # UPDATE demo (assuming id=1 exists)
    updateStudentEmail(1, "john.newmail@gmail.com")

    # DELETE demo assuming student row exists
    deleteStudent(3)

    print("After:")
    getAllStudents()