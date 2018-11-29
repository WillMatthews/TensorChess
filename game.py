#!/usr/bin/python3

import chess
import os
from state import State
from flask import Flask

app = Flask(__name__)

@app.route("/")
def webpage():
    ret = open("index.html").read()
    return ret

if __name__ == "__main__":
    s = State()
    winner = s.gameloop()
    if winner:
        winstr = "White"
    else:
        winstr = "Black"
    print(winstr + " Wins!")
