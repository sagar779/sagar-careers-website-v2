from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_sagar():
  job = load_jobs_from_db
  return render_template('home.html', jobs=job)


@app.route("/api/jobs")
def list_jobs():
  job = load_jobs_from_db()
  return jsonify(job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
