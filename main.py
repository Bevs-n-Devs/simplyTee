import os
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()                   # environment variables

app = Flask(__name__)           # config Flask app
app.secret_key = os.environ['SECRET_KEY']

# set up email configurations
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USE_TLS'] = os.environ['MAIL_USE_TLS']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']

# config for Flask-Mail
mail = Mail(app) 

# enable CORS
CORS(app)                       # extra layer of protection

@app.route('/')
def index():
    return render_template('home.html')


# contact Tolani via Contact Me section
@app.route('/contact', methods=['POST'])
def contact_tee():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        hairstyle = request.form.get('hairstyle')
        subject = request.form.get('Subject')
        message = request.form.get('Message')
        
        try:
            msg = Message(subject=f"New Enquiry from {name}",
                          sender=os.environ['MAIL_USERNAME'],
                          recipients=[os.environ['TOLANI_EMAIL']])  # Add your email here
            msg.body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Hairstyle: {hairstyle}
            Message: {message}
            """
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send message: {str(e)}', 'danger')

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(
        debug=False
    )