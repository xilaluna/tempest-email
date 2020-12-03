from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Home template
    """
    return render_template("base.html")


app.run(debug=True)
