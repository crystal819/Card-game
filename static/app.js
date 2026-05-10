console.log("hello")

const socket = io();

socket.emit("message", {
    text: "hello server"
});

socket.on("response", (data) => {
    console.log(data);
});

document.getElementById("btn1").addEventListener("click", () => {
    socket.emit("join_game");
    console.log("joining")
})

socket.on("game_state", (data) => {
    console.log(data);
});