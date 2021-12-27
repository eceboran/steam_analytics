import plotly.utils
from flask import render_template, flash, redirect, url_for, request
from app import app
import os
import sqlite3
import plotly.express as px
import json

# import pandas as pd

# Path of the current directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def home():
    # Create/connect to the database file
    file_name = "Games.db"
    conn = sqlite3.connect(os.path.join(current_directory, file_name))
    cursor = conn.cursor()

    # Top genres
    no_top_genres = 12
    sql_query = sql_query = f"""SELECT genre, COUNT(genre) as genre_count
    FROM(
    SELECT gms.steam_appid, gnr.genre, gms_gnr.genre_id, gms.total_reviews, gms.price_initial
    FROM
    games gms
    JOIN GamesGenresRelation gms_gnr ON gms.steam_appid = gms_gnr.steam_appid
    JOIN genres gnr ON gnr.genre_id = gms_gnr.genre_id)
    GROUP BY genre
    ORDER BY genre_count DESC
    LIMIT {no_top_genres}
    """
    #sql_query = "SELECT * FROM Games"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    genres = result

    names = [x[0] for x in genres]
    values = [x[1] for x in genres]
    fig = px.pie(values=values, names=names)

    graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('home.html', no_top_genres=no_top_genres, games=genres, graph1JSON=graph1JSON)


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
