from wtforms import SelectField, Form
from flask import Flask, render_template, request, session, flash, redirect, url_for
import sqlite3, os


app = Flask(__name__)


#TODO need to create a database with 4 fields and id will be the primary key and add the value by this add_details function and also need to show the details using another function
# provide hyperlink to go here and there and also create registration page and sync with the login

class SelectDetails(Form):
    choices = []
    for i in range(1,101):
        choices.append((i, i))
    marks = SelectField('Marks', choices=choices)



@app.route('/view_details')
def view_details():
    connection = sqlite3.connect('db/student_details.db')
    cursor = connection.cursor()
    sql = "Select * from student_details"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return render_template('show_details.html', rows=rows)



@app.route('/add_details', methods=['POST', 'GET'])
def add_details():
    form = SelectDetails()
    if request.method == 'POST':
        name = request.form.get('name')
        marks = request.form.get('marks')
        roll = request.form.get('roll')
        connection = sqlite3.connect('db/student_details.db')
        cursor = connection.cursor()
        # sql = "INSERT INTO student_details(Name, Marks, Roll) VALUES (?, ?, ?)",(name, marks, roll)
        cursor.execute("INSERT INTO student_details(Name, Marks, Roll) VALUES (?,?,?)",(name, marks, roll))
        connection.commit()
        print("VALUES GOT INSERTED")
    else:
        print('DATA NOT INSETED')
    return render_template('home.html', form = form)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:       
        return redirect(url_for('add_details'))

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)