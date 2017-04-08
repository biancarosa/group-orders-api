import unittest
import json
from api.builders.json_response_builder import JSONResponseBuilder
from api import app


class JSONResponseBuilderTest(unittest.TestCase):

    def test_build_json(self):
        data = ['my cool array']
        success = True
        message = ['Awesome message']
        with app.test_request_context():
            r = JSONResponseBuilder.build_response(data,
                                                   success, message)
        dictionary = json.loads(r.get_data().decode("utf-8"))
        self.assertEquals(dictionary['data'], data)
        self.assertEquals(dictionary['success'], success)
        self.assertEquals(dictionary['messages'], message)
