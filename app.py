from boggle import Boggle
from flask import Flask, request, render_template, session
import json
##from flask_debugtoolbar import DebugToolbarExtension



app=Flask("__boggle__")
app.debug = True
app.config['SECRET_KEY'] = 'my_key'
#toolbar = DebugToolbarExtension(app)
boggle_game = Boggle()



@app.route('/')
def main_page():  
    session['all_scores'] = []    
    
    session['board'] =boggle_game.board
    return render_template('base.html', board = boggle_game.board)


@app.route('/submit' , methods = ['POST'])
def form_submit():

    print(json.loads(request.data)['value'])
    submitted_word = json.loads(request.data)['value']

    checked_result = boggle_game.check_valid_word(session['board'],submitted_word) 
    
    return json.dumps({"result":checked_result})


all_scores = []

@app.route('/score', methods = ['POST'])
def score_submit():
    
    if type((session.get('all_scores'))) != 'list':
        session['all_scores'] = []    


    
    score = json.loads(request.data )['score']
    all_scores = session.get('all_scores')
    all_scores.append(score)



    session['all_scores'] = all_scores
    return json.dumps({"All Scores": all_scores, "Number of Attempts": len(all_scores),"Highest Score": max(all_scores)})
    
