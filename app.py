from flask import Flask , render_template
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



status=0

@app.route('/')
@app.route('/Home')
def homepage():
    global status
    return render_template('home.html',Status =status)

@app.route('/SignIn')
def sign_in_page():
    global status
    status= 0
    form = LoginForm()
    return render_template('home.html',Status =status,title = "Login Page", form=form)

@app.route('/SignUp')
def sign_up_page():
    global status
    status= 0
    return render_template('register.html',Status=status,title = "Register Page",form= form )



@app.route('/Profile')
def profile_page():
    global status
    status=1
    return render_template('home.html',Status=status)

@app.route('/Bag')
def bag_page():
    global status
    return render_template('home.html',Status =status)
   


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

