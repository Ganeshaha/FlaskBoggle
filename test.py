from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import json


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

        self.boggle_game = Boggle()
       # self.board = self.boggle_game.make_board()

    def test_homepage(self):
       with self.client as client:
        with client.session_transaction() as sess:
           # create a sample 2d array      
          
           response = client.get('/')
           html = response.get_data(as_text = True)
           
           self.assertEqual(response.status_code, 200)
           self.assertIn('form method="POST" id="guess-form">', html)

           sess['board'] =[['t','e','s','t'],
           ['t','e','s','t'],
           ['t','e','s','t'],
           ['t','e','s','t'],
           ['t','e','s','t']]
       
            #could not get the test to use the test board even when setting it in the session and pulling from session in app.py


           print(self.boggle_game.board)
           result = client.post('/submit',data = json.dumps({'value':'test'}))
           print(self.boggle_game.board)
           result_string = result.get_data(as_text = True)
      
           self.assertIn('result', result_string)
           self.assertIn('ok', result_string)

           # step 3 done

    def test_valid_score(self):
        with self.client as client:
            # result = client.post('/score',json = json.dumps({'score':300}))
            result = client.post('/score',json = {"score": 300})
            result_string = result.get_data(as_text = True)
            print(result_string)
            self.assertIn('All Scores', result_string)
            self.assertIn('Number of Attempts', result_string)
            self.assertIn('300', result_string)
            self.assertIn('Highest Score', result_string)
          
            #step 4 done
    def test_timer(self):
        with self.client as client:
        #unsure how to test timer
            return 


# ask about:
# debugging and finding variable
# adding a board to testing
# add board as an attribute to the boggle class, then change it in testing before server runs
