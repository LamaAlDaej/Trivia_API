import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = 'postgresql://postgres:d3V707L@localhost:5432/trivia_test'
        #self.database_path = "postgres://{}/{}@{}/{}".format('postgres','d3V707L','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        self.new_question = {
            'question': 'What is the nearest planet to the sun?',
            'answer': '',
            'difficulty': 1,
            'category': 1
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # TEST: GET /questions
    def test_get_paginated_questions(self):
        # Store the response in the 'res' variable
        res = self.client().get('/questions')
        # Load the data using json.loads of the response
        data = json.loads(res.data)

        # Check the status code is 200 
        self.assertEqual(res.status_code, 200)
        # Check the success body is true
        self.assertEqual(data['success'], True)
        # Assert true that there is a number of total questions
        self.assertTrue(data['total_questions'])
        # Assert true that there are questions in the data list
        self.assertTrue(len(data['questions']))

    # TEST: GET /questions?page=1000 (404: Page is not found)
    def test_404_sent_requesting_beyond_valid_page(self):
        # Store the response in the 'res' variable
        res = self.client().get('/questions?page=1000')
        # Load the data using json.loads of the response
        data = json.loads(res.data)

        # Check the status code is 404
        self.assertEqual(res.status_code, 404)
        # Check the success body is false
        self.assertEqual(data['success'], False)
        # Check the message body
        self.assertEqual(data['message'], 'The requested resource could not be found.')

    # TEST: DELETE /questions/7
    def test_delete_question(self):
        # Store the response in the 'res' variable (delete question 7)
        res = self.client().get('/questions/7')
        # Load the data using json.loads of the response
        data = json.loads(res.data)

        # Retrieve the question from the database (to check if it's no longer exist)
        question = Question.query.get(7).one_or_none()

        # Check the status code is 200
        self.assertEqual(res.status_code, 200)
        # Check the success body is true
        self.assertEqual(data['success'], True)
        # Check the deleted body to be the question id (7)
        self.assertEqual(data['deleted'], 7)
        # Assert true that there is a number of total questions
        self.assertTrue(data['total_questions'])
        # Assert true that there are questions in the data list
        self.assertTrue(len(data['questions']))
        # Check the question no longer exist
        self.assertEqual(question, None)

    # TEST: DELETE /questions/1000 (404: Resorce is not found)
    def test_404_if_question_does_not_exist(self):
        # Store the response in the 'res' variable
        res = self.client().get('/questions/1000')
        # Load the data using json.loads of the response
        data = json.loads(res.data)

        # Check the status code is 404
        self.assertEqual(res.status_code, 404)
        # Check the success body is false
        self.assertEqual(data['success'], False)
        # Check the message body
        self.assertEqual(data['message'], 'The requested resource could not be found.')

    # TEST: POST /questions
    def test_create_new_question(self):
        # Store the response in the 'res' variable
        res = self.client().get('/questions')
        # Load the data using json.loads of the response
        data = json.loads(res.data)

        # Check the status code is 200
        self.assertEqual(res.status_code, 200)
        # Check the success body is true
        self.assertEqual(data['success'], True)
        # Assert true that there is a number of total questions
        self.assertTrue(data['total_questions'])
        # Assert true that there are questions in the data list
        self.assertTrue(len(data['questions']))

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
