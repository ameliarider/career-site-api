from flask import Flask, request
import db
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/jobs.json")
def index():
    return db.jobs_all()

@app.route("/jobs.json", methods=["POST"])
def create():
    if request.is_json:
        data = request.json
    else:
        data = request.form
    
    title = data.get("title")
    company = data.get("company")
    location = data.get("location")
    description = data.get("description")
    salary = data.get("salary")
    return db.jobs_create(title, company, location, description, salary)

@app.route("/jobs/<id>.json")
def show(id):
    return db.jobs_find_by_id(id)

@app.route("/jobs/<id>.json", methods=["PATCH"])
def update(id):
    if request.is_json:
        data = request.json
    else:
        data = request.form
    current_job = db.jobs_find_by_id(id)

    title = request.args.get("title", current_job["title"])
    company = request.args.get("company", current_job["company"])
    location = request.args.get("location", current_job["location"])
    description = request.args.get("description", current_job["description"])
    salary = request.args.get("salary", current_job["salary"])
    return db.jobs_update_by_id(id, title, company, location, description, salary)

@app.route("/jobs/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.jobs_destroy_by_id(id)
