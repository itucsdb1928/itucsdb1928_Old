from flask import Flask ,redirect, render_template,flash,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

status=0

@app.route('/')
@app.route('/Home')
def homepage():
    global status
    return render_template('home.html',Status =status,title = "Home Page")

@app.route('/SignIn')
def sign_in_page():
    global status
    status= 0
    form = LoginForm()
    return render_template('login.html',Status =status,title = "Login Page", form=form)

@app.route('/SignUp',methods=['GET','POST'])
def sign_up_page():
    global status
    status= 0
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('homepage'))
    return render_template('register.html',Status=status,title = "Register Page",form= form )



@app.route('/Profile')
def profile_page():
    global status
    status=1
    return render_template('home.html',Status=status,title = "Profile Page")

@app.route('/Bag')
def bag_page():
    global status
    return render_template('home.html',Status =status,title = "Bag Page")
   


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

