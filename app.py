from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Home template
    """
    return render_template("home.html")


@app.route('/email')
def email():
    """
    Email page for 
    """
    return render_template("email.html")


@app.route('/login')
def login():
    """
    Login page
    """
    return render_template("auth/login.html")


app.run(debug=True)
