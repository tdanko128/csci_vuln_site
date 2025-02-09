from flask import Blueprint, render_template, request, Response
import os

frontend = Blueprint('frontend', __name__, template_folder='templates/frontend')

@frontend.route('/')
def home():
    return render_template('index.html')

@frontend.route('/about')
def about():
    return render_template('about.html')

@frontend.route('/contact', methods=['GET','POST'])
def contact():
    output = ''
    message = ''
    if request.method == 'POST':
        command =  request.form['subject']
        # Vulnerable to Command Injection
        output = os.popen(command).read()
        message = request.form['message']
    return render_template('contact.html', output=output, message=message)

@frontend.route('/team')
def team():
    rendered = render_template('team.html')
    response = Response(rendered)
    response.headers["X-Random"] = "ThisFunkyChicken"
    return response

@frontend.route('/team/<member>')
def team_member(member):
    return render_template(f'team/{member}.html', member=member)
