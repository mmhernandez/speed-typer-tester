from flask_app import app  
from flask import url_for, render_template

@app.route("/")
def index():
    return render_template("index.html")