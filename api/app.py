from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/groups', methods=['GET'])
def get_groups():
    response = {
        "success": True,
        "data": [],
        "messages": []
    }
    return jsonify(response), 200


@app.route('/groups', methods=['POST'])
def create_a_group():
    post_data = request.get_json()
    response = {
        "success": True,
        "data": {
            "id": "id",
            "name": post_data['name'],
            "createdAt": "",
            "estimatedCloseDate": post_data['estimatedCloseDate'],
            "status": "OPEN",
            "comments": post_data['comments'],
            "href": "/groups/id"
        },
        "messages": ['Created with success!']
    }
    return jsonify(response), 201
