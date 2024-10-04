from re import DEBUG
from flask import Flask, render_template 


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/experience")
def experience():
    return render_template("exp.html")

@app.route( "/projects")
def projects():
    return render_template("pj.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5002)