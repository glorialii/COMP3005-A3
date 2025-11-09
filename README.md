 # COMP3005 A3 — Students CRUD (PostgreSQL + Python)

 # make sure 2 install
- PostgreSQL (I am using pgAdmin 4 to run SQL)
- Python
- psycopg2 (pip install psycopg2-binary) in terminal

# Functionality
Implements CRUD against a `students` table with:
- `getAllStudents()`
- `addStudent(first_name, last_name, email, enrollment_date)`
- `updateStudentEmail(student_id, new_email)`
- `deleteStudent(student_id)`
(As reqrd by the assignment)

# How to steup
1) In pgAdmin, create DB `studentsdb`.  
2) Open Query Tool on `studentsdb`, run everything in `db_setup.sql`.  
3) Python:
```bash
pip install -r requirements.txt
