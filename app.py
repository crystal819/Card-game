from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
from cards import Game

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

games = {}


@app.route("/")
def home():
    return render_template("index.html")


@socketio.on("message")
def handle_message(data):
    print("Received:", data)

    emit("response", {
        "reply": "hello client"
    })

@socketio.on("join_game")
def join_game(data):

    game_id = data["game_id"]

    join_room(game_id)

    if game_id not in games:
        games[game_id] = Game()

    emit(
        "game_state",
        games[game_id].get_state(),
        room=game_id
    )

if __name__ == "__main__":
    socketio.run(app, debug=True)