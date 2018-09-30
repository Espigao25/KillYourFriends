var connection = new WebSocket('ws://192.168.0.101:9998')
var connectionReceive = new WebSocket('ws:/192.168.0.101:9997')

var players = [
    'Player1', 
    'Player2', 
    'Player3', 
    'Player4', 
    'Player5', 
    'Player6', 
    'Player7'
]

tick = () => {
    connection.send('heartbeat ' + new Date)
}

connection.onopen = () => {
    connection.send(players)
    setInterval(() => {tick()}, 1000)
}

connectionReceive.onmessage = (event) => {
    console.log(event.data)
}