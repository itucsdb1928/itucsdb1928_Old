from flask import Flask , render_template
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html',posts = x)

@app.route('/login')
def loginpage():
    form = LoginForm()
    return render_template('home.html', title = "Login Page", form=form)
   
@app.route('/register')
def registerpage():
       form = RegistrationForm()
       return render_template('register.html', title = "Register Page",form= form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

