from flask import Flask
from flask import render_template
import sql

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

app.run(debug=True)