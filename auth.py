from flask import Flask, Blueprint,render_template


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for handling login
    return render_template('login.html')