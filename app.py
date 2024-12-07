from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
DATABASE = 'database/students.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        """)

@app.route("/")
def index():
    with sqlite3.connect(DATABASE) as conn:
        students = conn.execute("SELECT * FROM students").fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        return redirect("/")
    return render_template("add_student.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, id))
        return redirect("/")
    with sqlite3.connect(DATABASE) as conn:
        student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    return render_template("update_student.html", student=student)

@app.route("/delete/<int:id>")
def delete_student(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM students WHERE id=?", (id,))
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(port=5001)
