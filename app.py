from flask import Flask, request
import db
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/jobs.json")
def index():
    return db.jobs_all()

@app.route("/jobs.json", methods=["POST"])
def create():
    title = request.form.get("title")
    company = request.form.get("company")
    location = request.form.get("location")
    description = request.form.get("description")
    salary = request.form.get("salary")
    return db.jobs_create(title, company, location, description, salary)