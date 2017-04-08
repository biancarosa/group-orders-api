import unittest
import os

class GroupsTest(unittest.TestCase):

    def setUp(self):
        self.api_url = os.environ['API_URL']        
