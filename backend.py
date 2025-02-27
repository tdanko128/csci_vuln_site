from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

backend = Blueprint('backend', __name__, template_folder='templates/backend')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@backend.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    username = request.args.get('username') if request.method == 'GET' else request.form.get('username')
    password = request.args.get('password') if request.method == 'GET' else request.form.get('password')


    if username:
        conn = sqlite3.connect('ethreal_realm.db')
        c = conn.cursor()

        # 🚨 Vulnerable to SQL Injection
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hash_password(password)}'"
        print(f"Executing query: {query}")  # Debugging SQL queries
        c.execute(query)
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('backend.dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'

    return render_template('login.html', error=error)


@backend.route('/dashboard')
@backend.route('/')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('backend.login'))

@backend.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('frontend.home'))

@backend.route('/execute', methods=['GET', 'POST'])
def execute():
    output = ''
    if request.method == 'POST':
        command = request.form['command']
        # Vulnerable to Command Injection
        output = os.popen(command).read()

    return render_template('execute.html', output=output)
