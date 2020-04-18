from flask import render_template, url_for, flash, redirect, request
import json
from khub.models import User, CameraGroup, Camera
from khub import app, db, bcrypt
from khub.forms import CreateUserForm, SignInForm
from flask_login import login_user, current_user, logout_user, login_required

# Config JSON
config_json = '''{
    "site": "Home",
    "viewport": { "width": 640, "height": 480},
    "cameras": [
        {
            "name": "Camera 1",
            "location": "Rumpus Room",
            "url": "http://192.168.1.61:8889/"
        },
        {
            "name": "Camera 2",
            "location": "Entrance and Stairs",
            "url": "http://192.168.1.6:8889/"
        }
    ]
}
'''

config = json.loads(config_json)

#camera_group = CameraGroup.query.filter_by(name='Home').first()


@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard", config=config)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/create_user", methods=['GET', 'POST'])
def create_user():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = CreateUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'User created for {form.username.data}!', category='success')
        return redirect(url_for('sign_in'))
    return render_template("create_user.html", title="CreateUser", form=form)

@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # args is a dict but use get() instead of ['next'] so it works if key does exist
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Sign In failed. Please check Username and Password', category='danger')
    return render_template("sign_in.html", title="SignIn", form=form)


@app.route("/sign_out")
def sign_out():
    logout_user()
    return redirect(url_for('sign_in'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")