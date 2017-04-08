from flask import jsonify


class JSONResponseBuilder(object):

    @staticmethod
    def build_response(data=[], success=True, messages=[]):
        response = {
            'data': data,
            'success': success,
            'messages': messages
        }
        return jsonify(response)
