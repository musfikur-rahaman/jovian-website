from re import DEBUG
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Dhaka',
    'Salary': 'USD 85,000'
}, {
    'id': 2,
    'title': 'Web Developer',
    'location': 'Dhaka',
}, {
    'id': 3,
    'title': 'Project Manager',
    'location': 'Dhaka',
    'Salary': 'USD 105,000'
}]


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)


@app.route("/experience")
def experience():
    return render_template("exp.html", jobs=JOBS)


@app.route("/projects")
def projects():
    return render_template("pj.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5002)
