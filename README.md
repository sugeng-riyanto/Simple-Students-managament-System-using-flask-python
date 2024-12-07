
# **Student Management System**

A simple and user-friendly web-based application to manage student records. This system allows users to view, add, edit, and delete student data. Built using **Python**, **Flask**, **SQLite**, **HTML**, and **CSS**, this project is perfect for learning and implementing CRUD operations in a web environment.

----------

## **Concepts: Python and Flask**

### **Python**

Python is a high-level, versatile programming language widely used for web development, data science, automation, and more. Some key concepts relevant to this project:

1.  **Functions**: Python uses functions to group code for specific tasks.
    -   Example: `def add_student(name, age, grade):` groups the logic for adding a student.
2.  **Modules and Libraries**: Python allows importing reusable code via libraries.
    -   Example: `import sqlite3` for database interactions and `from flask import Flask` for web development.
3.  **Object-Oriented Programming (OOP)**: Flask is an object-oriented framework where components like `app` behave as objects.

### **Flask**

Flask is a lightweight, easy-to-learn Python web framework. It enables developers to build web applications quickly and efficiently.

Key Flask concepts in this project:

1.  **Flask Application**:
    
    -   A Flask app is an object created using `Flask(__name__)`.
    -   Example:
        
        python        
        Copy code
        
        ```python
        from flask import Flask
        app = Flask(__name__)
        ```
        
2.  **Routes**:
    
    -   Routes define the URLs the app will respond to and their associated logic.
    -   Example:
        
        python
        
        Copy code
        
        ```python
        @app.route('/')
        def home():
            return "Welcome to the Student Management System!"
        ``` 
        
3.  **Templates**:
    
    -   HTML templates dynamically generate web pages.
    -   Flask uses **Jinja2 templating**, allowing Python code to run within HTML.
    -   Example:
        
        html
        
        Copy code
        
        ```html
        <h1>Welcome, {{ student_name }}</h1>
        ``` 
       
4.  **HTTP Methods**:
    
    -   **GET**: Fetch data (e.g., view students).
    -   **POST**: Send data to the server (e.g., add a new student).
    -   Example:
        
        python
        
        Copy code
        
        ```python
        @app.route('/add', methods=['GET', 'POST'])
        def add_student():
            if request.method == 'POST':
                # Add student logic
        ``` 
        
5.  **Database Integration**:
    
    -   Flask integrates seamlessly with databases like SQLite.
    -   Example:
        
        python
        
        Copy code
        
        ```python
        import sqlite3
        conn = sqlite3.connect('students.db')
        ``` 
        
----------

## **Features**

-   **View Students**: Display a list of all students with their details.
-   **Add Students**: Add new students by filling out a simple form.
-   **Update Students**: Edit existing student records, including their name, age, and grade.
-   **Delete Students**: Remove student records from the database.
-   **Responsive Design**: Clean and user-friendly interface styled with CSS.

----------

## **Project Structure**

![Result](https://github.com/sugeng-riyanto/Simple-Students-managament-System-using-flask-python/blob/main/Student%20Management%20System.png)

Here’s an overview of the project files and folders:

php

Copy code

```student_management/
├── static/
│   ├── css/
│   │   └── styles.css       # CSS file for styling the app
├── templates/
│   ├── base.html            # Base layout for all pages
│   ├── index.html           # Home page to display students
│   ├── add_student.html     # Page for adding a new student
│   ├── update_student.html  # Page for editing student details
├── app.py                   # Main Flask application file
├── database/
│   └── students.db          # SQLite database file
├── requirements.txt         # List of Python dependencies
└── README.md                # Documentation file` 
```
----------

## **Python and Flask in the Project**

### **1. Setting Up a Flask App**

The `app.py` file initializes a Flask app and defines routes for the application:

python

Copy code

```python
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

### **2. Working with Templates**

Templates like `index.html` dynamically display data using **Jinja2** syntax:

html

Copy code

```css
<table>
    {% for student in students %}
    <tr>
        <td>{{ student.name }}</td>
        <td>{{ student.age }}</td>
        <td>{{ student.grade }}</td>
    </tr>
    {% endfor %}
</table>
```


### **3. Integrating with SQLite**

SQLite is a lightweight database used to store student records. Python's `sqlite3` module is used for database operations:

python

Copy code

```python
def get_students():
    with sqlite3.connect("students.db") as conn:
        return conn.execute("SELECT * FROM students").fetchall()
``` 

### **4. Adding Routes**

Routes link URLs to specific Python functions. Flask routes support dynamic data handling:

python

Copy code

```python
@app.route("/delete/<int:id>")
def delete_student(id):
    with sqlite3.connect("students.db") as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (id,))
    return redirect("/")
``` 

----------

## **Setup Instructions**

### **Step 1: Clone or Download the Project**

bash

Copy code

```gitbash git clone https://github.com/your-username/student-management-system.git
cd student-management-system
``` 

----------

### **Step 2: Set Up a Virtual Environment**

(Optional but recommended)

bash

Copy code

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
``` 

----------

### **Step 3: Install Dependencies**

bash

Copy code

```terminal
pip install -r requirements.txt
``` 

----------

### **Step 4: Run the Application**

bash

Copy code

```bash
python app.py
``` 

Visit the app in your browser: `http://127.0.0.1:5000`.

----------

## **How It Works**

### **Home Page**

-   Displays a list of all students in the database.
-   Links to add, edit, or delete student records.

### **Adding a Student**

-   Fill in the form with student details (name, age, grade).
-   Submit to save the record in the database.

### **Editing a Student**

-   Click "Edit" next to a student record.
-   Update the details and submit the form.

### **Deleting a Student**

-   Click "Delete" to remove the student record permanently.

----------

## **Troubleshooting**

### **1. Port Conflict**

-   If another app is using the same port, change it in `app.py`:
    
    python
    
    Copy code
    
    `app.run(debug=True, port=5001)` 
    

### **2. Missing Database**

-   Ensure the `database/` folder exists.
-   Run the app to initialize the database.

----------

## **Further Learning**

To explore more about Python and Flask:

-   **Python Official Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
-   **Flask Documentation**: https://flask.palletsprojects.com/

----------

## **Contact**

If you have questions or need help:

-   **Email**: srphysics04@gmail.com
-   **GitHub**: https://github.com/sugeng-riyanto/ 
