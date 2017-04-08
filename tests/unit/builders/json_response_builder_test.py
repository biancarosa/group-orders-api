import unittest
import json
from api.builders.json_response_builder import JSONResponseBuilder
from api import app


class JSONResponseBuilderTest(unittest.TestCase):

    def test_build_json_with_success(self):
        data = ['my cool array']
        success = True
        with app.test_request_context():
            r = JSONResponseBuilder.build_response(data,
                                                   success)
        dictionary = json.loads(r.get_data().decode("utf-8"))
        self.assertEquals(dictionary['data'], data)
        self.assertEquals(dictionary['success'], success)
        self.assertEquals(dictionary['messages'], [])

    def test_build_json_without_success(self):
        success = False
        messages = ['Falhou']
        with app.test_request_context():
            r = JSONResponseBuilder.build_response(success=success,
                                                   messages=messages)
        dictionary = json.loads(r.get_data().decode("utf-8"))
        self.assertEquals(dictionary['data'], [])
        self.assertEquals(dictionary['success'], success)
        self.assertEquals(dictionary['messages'], messages)
