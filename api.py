import algorithm
from flask import *
import json

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def test_post():
    request_data = request.get_json()
    gm = []

    data=json.dumps(request_data)
    collection = json.loads(data)
    
    for i in collection['games']:
        gm.append(i)
    recs = algorithm.give_reccomendations(gm)

    return jsonify(game = recs)

app.run(port=3000)