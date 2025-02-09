from flask import Blueprint, render_template, request, send_from_directory
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
    return render_template('team.html')

@frontend.route('/team/<member>')
def team_member(member):
    return render_template(f'team/{member}.html', member=member)

@frontend.route('/events')
def events():
    return render_template('events.html')

@frontend.route('/events/wmh')
def download_flyer():
    return (send_from_directory('static/images','Event.jpg'))