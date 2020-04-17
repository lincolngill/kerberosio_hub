from flask import render_template, url_for, flash, redirect
import json
from khub.models import User, CameraGroup, Camera
from khub import app
from khub.forms import CreateUserForm, SignInForm

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
    form = CreateUserForm()
    if form.validate_on_submit():
        flash(f'User created for {form.username.data}!', category='success')
        return redirect(url_for('dashboard'))
    return render_template("create_user.html", title="CreateUser", form=form)

@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('Signed in!', category='success')
            return redirect(url_for('dashboard'))
        else:
            flash('Sign In failed. Please check Username and Password', category='danger')
    return render_template("sign_in.html", title="SignIn", form=form)