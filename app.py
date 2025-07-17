from flask import Flask, request
import db

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/jobs.json")
def index():
    return db.jobs_all()