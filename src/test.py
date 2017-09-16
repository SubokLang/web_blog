from flask import Flask, render_template, request, session
from src.models.user import User
from src.common.database import Database

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def hello_method():
    return render_template('login.html')

@app.route('/login')
def login_user():
    email = request.form['email']
    password = request.form['password']
    pass

    return render_template('profile.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
