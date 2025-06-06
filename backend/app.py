from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.post('/ai/move')
def ai_move():
    data = request.get_json()
    board = data.get('board', [])
    # board is list of 24 values: 0 empty, 1 user, 2 ai
    empty_positions = [i for i, v in enumerate(board) if v == 0]
    if not empty_positions:
        return jsonify({'position': None})
    position = random.choice(empty_positions)
    return jsonify({'position': position})

if __name__ == '__main__':
    app.run(debug=True)
