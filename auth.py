from flask import Flask, Blueprint,render_template,request,redirect
from config import Config

auth = Blueprint('auth', __name__)
config = Config()
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        _username = config.get('App', 'username')
        _password = config.get('App', 'password')
        # Here you would typically check the username and password against a database
        if username == _username and password == _password:
            return redirect('/admin/dashboard')
        else:
            return redirect('/auth/login?error=Invalid credentials')
    else:    
        return render_template('login.html')