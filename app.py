from flask import Flask, redirect, render_template,flash,url_for,current_app,request
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

UserId=0 # for navigation bar view
@app.route('/')
@app.route('/Home')
def homepage():
    global UserId
    My_list=db.get_home_page()
    return render_template('home.html',Status =UserId,title = "Home Page",titles=My_list)


@app.route('/SignIn',methods=['GET','POST'])
def sign_in_page():
    global UserId
    UserId= 0
    check = True
    form = LoginForm()
    if form.validate_on_submit():
        UserId = db.checkLogin(form.email.data,form.password.data)
        if UserId > 0:
            flash('Başarılı bir şekilde giriş yaptınız!', 'success')
            return redirect(url_for('profile_page'))
    
    return render_template('login.html',Status =UserId,title = "SıgnIn Page", form=form)

@app.route('/SignUp',methods=['GET','POST'])
def sign_up_page():
    global UserId
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        UserId =  db.insertNewUser(form)
        print(UserId)
        if UserId > 0:
             render_template('profile.html',Status=UserId,title = "Profile Page")

    return render_template('register.html',Status=UserId,title = "SıgnUp Page",form= form )

@app.route('/Profile')
def profile_page():
    global UserId
    print(" User Id In profile func",UserId)
    return render_template('profile.html',Status=UserId,title = "Profile Page")

@app.route('/Detail',methods=['GET','POST'])
def detail_page():
    global UserId
    if request.method == "POST":
        book_name=request.form["Book_name"]
        print(book_name)
        book_detail=db.get_detail_page(book_name)
        print(book_detail)
        return render_template('detail.html',Status=UserId,title = " %s Detail Page"%(book_name),details=book_detail,name=book_name)
    return render_template('home.html',Status =UserId,title = "Home Page")


if __name__ == '__main__':
    
    app.run(debug=True, use_reloader=True)
