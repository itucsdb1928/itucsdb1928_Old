from flask import Flask ,redirect, render_template,flash,url_for,current_app,request
from forms import RegistrationForm,LoginForm
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from urllib.parse import urlparse
import os
import psycopg2 as dbapi2
from arrangement import Database
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


db=Database()

status=0 # for navigation bar view

my_list = ["x","t"]
@app.route('/')
@app.route('/Home')
def homepage():
    global status
    My_list=db.get_home_page()
    return render_template('home.html',Status =status,title = "Home Page",results=my_list)

@app.route('/SignIn',methods=['GET','POST'])
def sign_in_page():
    global status
    status= 0
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'alihan@tutuk.com' and form.password.data == '1234':
            flash('Başarılı bir şekilde giriş yaptınız!', 'success')
            status=1
            return redirect(url_for('homepage'))
        else:
            flash('Giriş başarısız. Lütfen mailinizi veya şifrenizi kontrol edin.', 'danger')
            status=0
    return render_template('login.html',Status =status,title = "SıgnIn Page", form=form)

@app.route('/SignUp',methods=['GET','POST'])
def sign_up_page():
    global status
    status= 0
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        status=1
        return redirect(url_for('homepage'))
    return render_template('register.html',Status=status,title = "SıgnUp Page",form= form )



@app.route('/Profile')
def profile_page():
    global status
    status=1
    return render_template('home.html',Status=status,title = "Profile Page")




if __name__ == '__main__':
    
    app.run(debug=True, use_reloader=True)
