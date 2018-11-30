#!/usr/bin/python3

from state import State
from flask import Flask
from flask_sockets import Sockets
import json
import random
import time

app = Flask(__name__)
sockets = Sockets(app)


@app.route("/")
def webpage():
    ret = open("htmls/index.html").read()
    return ret


@app.route("/compvcomp")
def compvcomp():
    ret = open("htmls/compvcomp.html").read()
    return ret


@sockets.route("/chesssocket")
def chesssocket(ws):
    s = State()
    while not ws.closed:
        # parse the websocket for the move made by player
        message = ws.receive()
        print(message)
        msgdict = json.loads(message)
        gamemove = s.board.parse_san(msgdict["san"])
        s.board.push(gamemove)

        moves = s.engine_move()
        movestr = str(moves[0])
        move = s.uci_2_move(movestr)
        mv_socket = s.board.san(move)
        s.board.push(move)
        print("Move pushed to client: " + mv_socket)
        ws.send(mv_socket)


@sockets.route("/selfplay")
def chesssocket(wss):
    s = State()
    msg = wss.receive()
    while not wss.closed:
        time.sleep(0.4)
        setdepth = random.randint(1,4)
        moves = s.engine_move(search=setdepth)
        movestr = str(moves[0])
        move = s.uci_2_move(movestr)
        mv_socket = s.board.san(move)
        s.board.push(move)
        print("Move pushed to client: " + mv_socket)
        wss.send(mv_socket)


@app.route("/rand")
def randgame():
    ret = open("htmls/randgame.html").read()
    return ret


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
