from flask import Flask, request
import db
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/jobs.json")
def index():
    return db.jobs_all()

@app.route("/jobs.json", methods=["POST"])
def create():
    title = request.args.get("title")
    company = request.args.get("company")
    location = request.args.get("location")
    description = request.args.get("description")
    salary = request.args.get("salary")
    return db.jobs_create(title, company, location, description, salary)

@app.route("/jobs/<id>.json")
def show(id):
    return db.jobs_find_by_id(id)