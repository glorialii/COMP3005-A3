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

# Vid link
https://drive.google.com/file/d/1pyU764_sn7f0ooff7xPYDJzuERuaGZr5/view?usp=drive_link

# How to steup
1) In pgAdmin, create DB `studentsdb`.  
2) Open Query Tool on `studentsdb`, run everything in `db_setup.sql`.  
3) Go into terminal and cd to the correct folder with this code, this folder is named 'COMP3005_A3', then run 'python main.py', then you can check the output for the demo, you can alter the demo, and go into pgAdmin 4 to check the updated table.
pip install -r requirements.txt
