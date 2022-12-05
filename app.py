from flask import Flask, request, jsonify
from flask_dynamo import Dynamo
import json, random, string

app = Flask(__name__)
dynamo = Dynamo(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/create-user", methods=["POST"])
def create_user():
    try:
        request_data = json.loads(request.data)
        dynamo.tables['user_table'].put_item(Item={"id": ''.join(random.choices(string.ascii_letters + string.digits, k=4)),
                                                   "first_name": request_data["first_name"],
                                                   "last_name": request_data["last_name"],
                                                   "address": request_data["address"],
                                                   "email": request_data["email"]})
        print('HI')
        print(dynamo.tables['user_table'])
        return {"result": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.route('/update_user/<id>', methods=['POST'])
def update_user(id):
    try:
        request_data = json.loads(request.data)
        dynamo.tables['user_table'].update_item(
            Key={
                'id': id
            },
            UpdateExpression='SET first_name = :first_name, last_name = :last_name, address = :address, email = :email',
            ExpressionAttributeValues={
                ":first_name": request_data["first_name"],
                ":last_name": request_data["last_name"],
                ":address": request_data["address"],
                ":email": request_data["email"]
            }
        )
        return {"result": "User updated successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.route("/get-user/<id>", methods=["GET"])
def get_user():
    try:
        user_details = dynamo.tables['user_table'].get_item(Key={'id': id})
        return {"result": user_details}
    except Exception as e:
        return {"error": str(e)}
    
