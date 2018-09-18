from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from os import walk



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

posts = [
    {

        'title': 'Username__________',

    },
    {

        'title': 'Password__________'
    }
]


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '1@d.com' and form.password.data == '2':
            flash('You have been logged in!', 'success')
            return redirect(url_for('allvm'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login1.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register1.html', title='Register', form=form)

@app.route("/allvm", methods=['GET', 'POST'])
def allvm():
    for dirpath, dirnames, filenames in walk('/Users/thanawatruchasiri/Desktop/Song') :
        break
    return render_template('allVM.html', posts=posts, my_list=[filenames])


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/createvm")
def createvm():
    return render_template('createVM.html', title='createVM', my_list=['a','b','c'])

@app.route("/deployvm")
def deployvm():
    return render_template('deployVM.html', title='createVM')

if __name__ == '__main__':
    app.run(debug=True)
