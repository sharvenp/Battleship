from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from battleship_bot import BattleshipBot

bot = BattleshipBot()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/vector-api/get-configuration', methods=['GET'])
def get_configuration():
    config = bot.get_configuration();
    return (jsonify(config), 200)

@app.route('/vector-api/get-move', methods=['GET', 'POST'])
def get_move():
    grid = json.loads(request.data)['grid']
    move = bot.get_move(grid);
    return ({"i": move[0], "j": move[1] }, 200)


if __name__ == '__main__':
    app.run('0.0.0.0', 8081, debug=True)