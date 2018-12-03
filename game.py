#!/usr/bin/python3

from state import State
from flask import Flask
from flask_sockets import Sockets
import json
import random
import time
#import Threading

app = Flask(__name__)
sockets = Sockets(app)


#### WEB PAGES

@app.route("/")
def webpage():
    ret = open("htmls/index.html").read()
    return ret


@app.route("/stockself")
def compvcomp():
    generic = open("htmls/generic.html").read()
    brd  = open("htmls/stockself.html").read()
    return generic.replace("<!--placeboard-->",brd)


@app.route("/stocksurvive")
def stockfish_survival():
    generic = open("htmls/generic.html").read()
    brd  = open("htmls/stocksurvive.html").read()
    return generic.replace("<!--placeboard-->",brd)


@app.route("/rand")
def randgame():
    generic = open("htmls/generic.html").read()
    brd  = open("htmls/randboard.html").read()
    return generic.replace("<!--placeboard-->",brd)



####### WEBSOCKETS

@sockets.route("/chesssocket")
def stockfish_survival_socket(ws):
    s = State()
    while not ws.closed and not s.board.is_game_over():
        setdepth = 2 # MAKE THIS VALUE USER CONFIGURABLE
        if s.board.is_game_over():
            print("Closing Socket")
            wss.close() # this does not close the socket for some reason?

        # parse the websocket for the move made by player
        message = ws.receive()
        print(message)
        msgdict = json.loads(message)
        gamemove = s.board.parse_san(msgdict["san"])
        s.board.push(gamemove)
        time.sleep(0.3)
        moves = s.stockfish_move(search=setdepth)
        movestr = str(moves[0])
        move = s.uci_2_move(movestr)
        mv_socket = s.board.san(move)
        s.board.push(move)
        print("Move pushed to client: " + mv_socket)
        #print(s.board)
        ws.send(mv_socket)


@sockets.route("/selfplay")
def stockfish_selfplay_socket(wss):
    s = State()
    msg = wss.receive()
    while not wss.closed:
        if s.board.is_game_over():
            print("Closing Socket")
            wss.close() # this does not close the socket for some reason?
        print(msg)
        time.sleep(0.4)
        setdepth = random.randint(1,6)
        moves = s.stockfish_move(search=setdepth)
        movestr = str(moves[0])
        move = s.uci_2_move(movestr)
        mv_socket = s.board.san(move)
        s.board.push(move)
        print("Move pushed to client: " + mv_socket)
        #print(s.board)
        wss.send(mv_socket)
        msg = wss.receive()




###### DEBUG


@app.route("/sockettest")
def socket_test():
    ret  = open("htmls/sockettest.html").read()
    return ret


@sockets.route("/echosocket")
def echo(wse):
    while not wse.closed:
        msg = wse.receive()
        wse.send(msg)



##### server main

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
