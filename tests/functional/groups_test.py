import unittest
import os
import requests


class GroupsTest(unittest.TestCase):

    def setUp(self):
        self.api_url = os.environ['API_URL']

    def test_get_groups(self):
        req = requests.get(self.api_url + '/groups')
        data = req.json()

        self.assertEquals(req.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertIsNotNone(data['data'])
        self.assertEqual(len(data['messages']), 0)

    def test_create_a_group(self):
        request_data = {
           "name": "string",
           "estimatedCloseDate": "2017-04-06 16:57:00",
           "comments": "string"
        }
        req = requests.post(self.api_url + '/groups',
                            headers={"Content-type": "application/json"},
                            json=request_data)
        data = req.json()

        self.assertEqual(req.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['messages']), 1)
        self.assertIsNotNone(data['data']['id'])
        self.assertEquals(data['data']['name'], request_data['name'])
        self.assertIsNotNone(data['data']['createdAt'])
        self.assertEqual(data['data']['estimatedCloseDate'],
                         request_data['estimatedCloseDate'])
        self.assertEqual(data['data']['status'], 'OPEN')
        self.assertEqual(data['data']['comments'], request_data['comments'])
        self.assertEqual(data['data']['href'], '/groups/'+data['data']['id'])
