from api import app
from flask import request
from api.builders.json_response_builder import JSONResponseBuilder


@app.route('/groups', methods=['GET'])
def get_groups():
    return JSONResponseBuilder.build_response(
        success=True,
        data=[]
    ), 200


@app.route('/groups', methods=['POST'])
def create_a_group():
    post_data = request.get_json()
    return JSONResponseBuilder.build_response(
        success=True,
        data={
            "id": "id",
            "name": post_data['name'],
            "createdAt": "",
            "estimatedCloseDate": post_data['estimatedCloseDate'],
            "status": "OPEN",
            "comments": post_data['comments'],
            "href": "/groups/id"
        },
        messages=['Created with success!']
    ), 201
