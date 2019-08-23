import os
from flask import Flask
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError
from forms import LoginForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return "123"
    return render_template('basic.html', form=form)


app.run()