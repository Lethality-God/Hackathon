import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

db = sqlite3.connect('database.db', check_same_thread=False)
c = db.cursor()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_type = request.form.get('user_type')
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        flash('Please enter both username and password', 'error')
        return redirect(url_for('index'))
    
    # Here you would typically validate against a database
    # For now, we'll just show a success message
    if user_type == 'student':
        c.execute("SELECT password, roll_no FROM student_records WHERE name = ?", (username,))
        credentials = c.fetchone()
        if credentials:
            print(credentials)
            if credentials[0] == password:
                # Store student roll number in session
                session['student_roll_no'] = credentials[1]
                session['student_name'] = username
                return redirect(url_for('student_dashboard'))
            else:
                flash('Invalid password', 'error')


    return redirect(url_for('index'))

@app.route('/student_dashboard')
def student_dashboard():
    # Check if student is logged in
    if 'student_roll_no' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('index'))
    
    roll_no = session.get('student_roll_no')
    student_name = session.get('student_name')
    return render_template('student_dashboard.html', roll_no=roll_no, student_name=student_name)

@app.route('/my_courses')
def my_courses():
    # Check if student is logged in
    if 'student_roll_no' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('index'))
    
    roll_no = session.get('student_roll_no')
    student_name = session.get('student_name')
    
    # TODO: Fetch actual courses from database based on student
    c.execute("SELECT semester FROM student_records WHERE roll_no = ?", (roll_no,))
    semester = c.fetchone()[0]
    c.execute("SELECT * FROM courses WHERE semester = ?", (semester,))
    courses = c.fetchall()
    
    return render_template('my_courses.html', roll_no=roll_no, student_name=student_name, courses=courses)

@app.route('/grades')
def grades():
    # Check if student is logged in
    if 'student_roll_no' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('index'))
    
    roll_no = session.get('student_roll_no')
    student_name = session.get('student_name')
    

    c.execute("SELECT semester FROM student_records WHERE roll_no = ?;", (roll_no,))
    semester_result = c.fetchone()
    semester = semester_result[0] if semester_result else "N/A"
    
    marks_db = sqlite3.connect('exam_marks.db', check_same_thread=False)
    marks = marks_db.cursor();


    grades = []

    c.execute("SELECT code FROM courses")
    subjects = c.fetchall()

    for subject in subjects:
        temp = subject[0]
        course_code = ""
        for i in temp:
            if(i != '-'):
                course_code += i;
        query = f"SELECT * FROM `{course_code}` WHERE roll_no = ?"
        
        try:
            marks.execute(query, (roll_no,))
            temp = marks.fetchone()
            
            if temp:
                temp = list(temp)
                temp.pop(0)
                temp.insert(0, course_code)
                grades.append(temp)
        except Exception as e:
            print(f"Error querying course '{course_code}': {e}")

    print(grades)

        
    return render_template('grades.html', roll_no=roll_no, student_name=student_name, semester=semester, grades=grades)

@app.route('/register/student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'GET':
        return render_template('register_student.html')
    
    # TODO by user: Implement student registration backend logic
    # This should include:
    # 1. Validate form data (name, college, university, roll_number, email, password)
    # 2. Check if user already exists (by email or roll number)
    # 3. Hash password securely
    # 4. Save to database
    # 5. Send confirmation email (optional)
    # 6. Populate college and university dropdowns from database

    if request.method == 'POST':
        name = request.form.get('name')
        college = request.form.get('college')
        university = request.form.get('university')
        roll_number = request.form.get('roll_number')
        email = request.form.get('email')
        password = request.form.get('password')

        
    
    # Student registration validation
    name = request.form.get('name')
    college = request.form.get('college')
    university = request.form.get('university')
    roll_number = request.form.get('roll_number')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not all([name, college, university, roll_number, email, password]):
        flash('Please fill in all required fields for student registration.', 'error')
        return redirect(url_for('register_student'))
    
    flash(f'Student registration successful! Welcome {name}! You can now login.', 'success')
    return redirect(url_for('index'))

@app.route('/register/teacher', methods=['GET', 'POST'])
def register_teacher():
    if request.method == 'GET':
        return render_template('register_teacher.html')
    
    # TODO by user: Implement teacher registration backend logic
    
    # Teacher registration validation
    name = request.form.get('name')
    email = request.form.get('email')
    teacher_id = request.form.get('teacher_id')
    phone = request.form.get('phone')
    qualification = request.form.get('qualification')
    subject = request.form.get('subject')
    password = request.form.get('password')
    
    if not all([name, email, teacher_id, phone, qualification, subject, password]):
        flash('Please fill in all required fields for teacher registration.', 'error')
        return redirect(url_for('register_teacher'))
    
    flash(f'Teacher registration successful! Welcome {name}! You can now login.', 'success')
    return redirect(url_for('index'))

@app.route('/register/college', methods=['GET', 'POST'])
def register_college():
    if request.method == 'GET':
        return render_template('register_college.html')
    
    # TODO by user: Implement college registration backend logic
    
    # College registration validation
    college_name = request.form.get('college_name')
    email = request.form.get('email')
    college_id = request.form.get('college_id')
    phone = request.form.get('phone')
    address = request.form.get('address')
    website = request.form.get('website')
    password = request.form.get('password')
    
    if not all([college_name, email, college_id, phone, address, website, password]):
        flash('Please fill in all required fields for college registration.', 'error')
        return redirect(url_for('register_college'))
    
    flash(f'College registration successful! Welcome {college_name}! You can now login.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard/<user_type>')
def dashboard(user_type):
    return render_template('dashboard.html', user_type=user_type)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)