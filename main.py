from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    error_check = False
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    if username == '':
        username_error = "Please enter a username"
        error_check = True
    if " " in username:
        username_error = "Username cannot contain spaces"
        error_check = True
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
        error_check = True
    if ' ' in password or password == '':
        password_error = "Please enter a password"
        password = ''
        verify_password = ''
        error_check = True
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
        password = ''
        verify_password = ''
        error_check = True
    if password != verify_password:
        verify_password_error = "Passwords do not match"
        password = ''
        verify_password = ''
        error_check = True
    elif verify_password == '':
        verify_password_error = "Passwords do not match"
        error_check = True
    
    if email != '':
        if email.count('@') != 1:
            email_error = "Not a valid email address"
            error_check = True
        if email.count('.') != 1:
            email_error = "Not a valid email address."
            error_check = True
        if " " in email:
            email_error = "Not a valid email address."
            error_check = True
        elif len(email) < 3 or len(email) > 20:
            username_error = "Email must be between 3 and 20 characters"
            error_check = True

    if error_check == True:
        return render_template('home.html', username_error=username_error,
            password_error=password_error, verify_password_error=verify_password_error,
            email_error=email_error, username=username, password=password,
            verify_password=verify_password, email=email)
    else:
        return render_template('welcome.html', username=username)
app.run()