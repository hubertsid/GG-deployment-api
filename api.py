import algo
from flask import *
import json

app = Flask(__name__)

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

    return jsonify(game = recs)

app.run()