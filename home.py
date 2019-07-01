from flask import Flask, render_template

app = Flask(__name__)


#TODO need to create a database with 4 fields and id will be the primary key and add the value by this add_details function and also need to show the details using another function
# provide hyperlink to go here and there and also create registration page and sync with the login
@app.route('/home')
def add_details():
    return render_template('home.html')