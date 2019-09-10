from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = '?????F???a?L`???$t?ǒ'

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def submit():
    if len(request.form['email']) < 1:
        flash('Email Cannot be Blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address')
    else:
        flash("Success! Your username is {}".format(request.form['email']))
    return redirect('/')

app.run(debug=True)