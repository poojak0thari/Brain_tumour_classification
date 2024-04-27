from pbl import app
from flask import render_template, url_for,redirect ,flash
from pbl.forms import RegistrationForm,LoginForm

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home page')

@app.route('/about')
def about():
    return render_template('about.html',title='Why Brainzy ')

@app.route('/detail')
def detail():
    return render_template('detail.html',title='More Details ')

@app.route('/upload')
def upload():
    return render_template('upload.html',title='Upload ')

@app.route('/signup' ,methods=['POST','GET'])
def signup():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created scccessfully for {form.username.data}' , category='success')
        return redirect(url_for('login'))
    return render_template('signup.html',title='Signup',form=form)

@app.route('/login' ,methods=['POST','GET'])
def login():
        form=LoginForm()
        if form.validate_on_submit():
             if form.email.data=='vidhi@gmail.com' and form.password.data=='123456':
                        flash(f'Login scccessful for {form.email.data}' , category='success')
                        return redirect(url_for('upload'))
             else:
                  flash(f'  Invalid Email-id or password' , category='danger')
        return render_template('login.html',title='Login',form=form)

@app.route('/review')
def review():
    return render_template('review.html',title='Review')

