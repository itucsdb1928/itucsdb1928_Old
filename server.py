from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def homepage():
    return """ <h1>Hello world</h1>""""


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

