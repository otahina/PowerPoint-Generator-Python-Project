import os
from flask import Flask, render_template, url_for, flash, redirect, request, send_from_directory, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from database import db
from models import User
from gpt_generate import chat_development
from text_pp import parse_response, create_ppt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
bcrypt = Bcrypt(app)
db.init_app(app)


# Configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', user=current_user)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form, user=current_user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if the user is already authenticated, redirect them to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form, user=current_user)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/generator', methods=['GET', 'POST'])
@login_required
def generate():
    if request.method == 'POST':
        number_of_slide = request.form['number_of_slide']
        user_text = request.form['user_text']
        template_choice = request.form.get('template_choice')
        presentation_title = request.form['presentation_title']

        user_message = f"I want you to come up with the idea for the power point. The number of slide is {number_of_slide}. " \
                       f"The content is: {user_text}. Can you summarize the content for each slide?"

        assistant_response = chat_development(user_message)
        print(assistant_response)
        slides_content = parse_response(assistant_response)
        create_ppt(slides_content, template_choice, presentation_title)

    return render_template('generator.html', title='Generate')


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory('generated', filename, as_attachment=True)

    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)
