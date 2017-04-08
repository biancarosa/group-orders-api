from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/groups', methods=['GET'])
def get_groups():
    response = {
        "success": True,
        "data": [],
        "messages": []
    }
    return jsonify(response), 200
