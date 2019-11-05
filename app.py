from flask import Flask , render_template
app = Flask(__name__)

x = [1,2,3,4,5]

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html',posts = x)

@app.route('/login')
def loginpage():
    return render_template('home.html', title = "Login Page")
   


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

