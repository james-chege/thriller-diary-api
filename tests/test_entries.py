# tests/test_entries.py

# For unit testing of entries

# standard unittest
import unittest
from app import create_app
# import Entry classe from models
from app.models import Entry
from flask import jsonify

class TestDiaryEntry(unittest.TestCase):
    """test for successful and unsuccessful entry addition"""
    def setUp(self):
        self.ent = Entry()
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.entry = {'title':'At Russia', 'description':'Me and my three friends decided ...'}
        self.entry_route = 'api/v1/entries/'

    def test_entry_adding_success(self):
        """returns True if entry addition was successful"""
        result = self.ent.add_entry("At Russia", "some good description of world cup experience")
        self.assertEqual(True, result)

    def test_entry_adding_failure(self):
    	"""returns False if an entry addition failed"""
    	result = self.ent.add_entry("title", "some")
    	self.assertFalse(False, result)

    def entry_add(self):
        return self.client().post(self.entry_route, headers=None, data=self.entry)

    def test_entry_creation(self):
        """Test entry creation via post method"""
        req = self.client().post(self.entry_route, headers=None, data=jsonify({'title':'At Russia', 'description':'Me and my three friends decided ...'}))
        self.assertEqual(req.status_code, 201)
        self.assertIn('At Russia',req.data)