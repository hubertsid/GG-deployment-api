import algo
from flask import *
import json
from flask_cors import CORS, cross_origin
import sqlite3

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()

@app.route('/')
def home_view():
    return "<h1>Welcome to gamer grandma</h1>"

@app.route('/api', methods=['POST'])
def test_post():
    request_data = request.get_json()
    gm = []

    data=json.dumps(request_data)
    collection = json.loads(data)
    
    for i in collection['games']:
        gm.append(i)

    recs = algo.give_reccomendations(gm)
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    
    for r in recs:
        query = "SELECT * FROM games WHERE title = ?"
        c.execute(query,r)
        result = c.fetchall()




    return jsonify(game = recs)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)