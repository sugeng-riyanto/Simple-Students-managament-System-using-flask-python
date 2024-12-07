# Import necessary modules from Flask and SQLite
from flask import Flask, render_template, request, redirect  # Flask: Web framework, request: handle form data, redirect: redirect users
import sqlite3  # SQLite3: Lightweight database module

# Create a Flask application instance
app = Flask(__name__)  # Initializes the Flask app

# Define the database file location
DATABASE = 'database/students.db'  # Path to the SQLite database file

# Function to initialize the database and create the "students" table if it doesn't exist
def init_db():
    with sqlite3.connect(DATABASE) as conn:  # Connect to the database
        conn.execute("""  # SQL query to create the students table
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each student
                name TEXT NOT NULL,  # Student's name (required)
                age INTEGER NOT NULL,  # Student's age (required)
                grade TEXT NOT NULL  # Student's grade (required)
            )
        """)

# Route for the home page
@app.route("/")  # Defines the URL for this function (http://127.0.0.1:5001/)
def index():
    # Fetch all student records from the database
    with sqlite3.connect(DATABASE) as conn:  # Connect to the database
        students = conn.execute("SELECT * FROM students").fetchall()  # Fetch all rows from the students table
    # Render the HTML template "index.html" and pass the student data
    return render_template("index.html", students=students)

# Route for adding a new student
@app.route("/add", methods=["GET", "POST"])  # Supports GET (load page) and POST (submit form)
def add_student():
    if request.method == "POST":  # If the form is submitted
        name = request.form["name"]  # Get the name input from the form
        age = request.form["age"]  # Get the age input from the form
        grade = request.form["grade"]  # Get the grade input from the form
        # Insert the new student into the database
        with sqlite3.connect(DATABASE) as conn:  # Connect to the database
            conn.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))  # Add student data
        return redirect("/")  # Redirect to the home page after adding the student
    return render_template("add_student.html")  # Render the add student form

# Route for updating an existing student
@app.route("/update/<int:id>", methods=["GET", "POST"])  # Supports GET (load page) and POST (submit form)
def update_student(id):  # Accepts the student's ID as a parameter
    if request.method == "POST":  # If the form is submitted
        name = request.form["name"]  # Get the updated name from the form
        age = request.form["age"]  # Get the updated age from the form
        grade = request.form["grade"]  # Get the updated grade from the form
        # Update the student record in the database
        with sqlite3.connect(DATABASE) as conn:  # Connect to the database
            conn.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, id))  # Update student data
        return redirect("/")  # Redirect to the home page after updating the student
    # If it's a GET request, fetch the student's current data to pre-fill the form
    with sqlite3.connect(DATABASE) as conn:  # Connect to the database
        student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()  # Fetch the student's data by ID
    return render_template("update_student.html", student=student)  # Render the update student form with current data

# Route for deleting a student
@app.route("/delete/<int:id>")  # Accepts the student's ID as a parameter
def delete_student(id):
    # Delete the student record from the database
    with sqlite3.connect(DATABASE) as conn:  # Connect to the database
        conn.execute("DELETE FROM students WHERE id=?", (id,))  # Delete the student by ID
    return redirect("/")  # Redirect to the home page after deletion

# Main entry point of the application
if __name__ == "__main__":  # Ensures the script runs only when executed directly
    init_db()  # Initialize the database (creates table if it doesn't exist)
    app.run(port=5001)  # Start the Flask app on port 5001 (accessible at http://127.0.0.1:5001/)
