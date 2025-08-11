from flask import Flask, Blueprint,render_template,request


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Here you would typically check the username and password against a database
        if username == 'admin' and password == 'admin':
            return render_template('admin/dashboard.html', username=username)
        else:
            return render_template('login.html', error='Invalid credentials')
    else:    
        return render_template('login.html')