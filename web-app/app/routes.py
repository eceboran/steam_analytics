from flask import render_template, flash, redirect, url_for, request
from app import app

def create_score_table():
    games_init = [
        {
            'name': 'Resident Evil',
            'score': '5.6'
        },
        {
            'name': "Assassin's Creed",
            'score': "6.3"
        }
    ]
    return games_init


@app.route('/')
def home():
    games = create_score_table()
    return render_template('home.html', games=games)


@app.route('/game_details', methods=['GET', 'POST'])
def game_details():
    if request.method == 'POST':
        new_rating = request.form["game_score"]
    else:
        new_rating = request.args.get('game_score')
    games = [
            {
                'name': 'Resident Evil',
                'score': new_rating
            },
            {
                'name': "Assassin's Creed",
                'score': "6.3"
            }
        ]
    return render_template("home.html", games=games)
