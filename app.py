from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

game = {
    "turn": "p1",
    "cards": ["2s", "3d"]
}


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
def join_game():
    print("player joined")
    emit("game_state", game)


if __name__ == "__main__":
    socketio.run(app, debug=True)