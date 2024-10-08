from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password') # type: ignore
    submit = SubmitField(label='Log in')
    
app = Flask(__name__)
app.secret_key = "cocheche"


@app.route("/")
def home():
    return render_template('index.html')
@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
