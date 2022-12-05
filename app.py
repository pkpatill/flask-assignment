from flask import Flask, request, jsonify
from flask_dynamo import Dynamo
import json

app = Flask(__name__)
dynamo = Dynamo()
dynamo.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/create-user", methods=["POST"])
def create_user():
    try:
        request_data = json.loads(request.data)
        dynamo.tables['user_table'].put_item(data={"first_name": request_data.first_name,
                                                   "last_name": request_data.last_name,
                                                   "address": request_data.address,
                                                   "email": request.email})
        return {"result": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.route("/update-user", methods=["POST"])
def update_user():
    try:
        request_data = json.loads(request.data)
        return {"result": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}

@app.route("/get-user", methods=["GET"])
def get_user():
    try:
        request_data = json.loads(request.data)

        return {"result": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}
