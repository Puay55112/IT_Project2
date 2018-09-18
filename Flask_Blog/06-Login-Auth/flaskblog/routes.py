from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from os import walk


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('allvm'))
    form = LoginForm()
    if form.email.data == '1@d.com' and form.password.data == '2':
        flash('You have been logged in!', 'success')
        return redirect(url_for('allvm_A'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('allvm'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login1.html', title='Login', form=form)



@app.route("/allvm", methods=['GET', 'POST'])
def allvm():
    for dirpath, dirnames, filenames in walk('/Users/thanawatruchasiri/Desktop/Song') :
        break
    return render_template('allVM.html', posts=posts, my_list=[filenames])

@app.route("/allvm_A", methods=['GET', 'POST'])
def allvm_A():
    return_vms = []
    for dirpath, dirnames, filenames in walk('/Users/thanawatruchasiri/Documents/Virtual_Machines') :

        print('....')
        print(filenames, "\n")
        print(dirnames, "\n")
        print(dirpath, "\n")


        return_vms.append(dirnames)
        break

    print(return_vms)

    return render_template('allVM_A.html', posts=posts, my_list=[return_vms])

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('allvm'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register1.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/createvm")
def createvm():
    return render_template('createVM.html', title='createVM', my_list=['a','b','c'])

@app.route("/deployvm")
def deployvm():
    return render_template('deployVM.html', title='createVM')


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
