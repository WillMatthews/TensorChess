#!/usr/bin/python3

import chess
import chess.svg
import chess.uci
import os
import random

clear = lambda: os.system('clear')

class State(object):
    def __init__(self,board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board
        self.engine =  chess.uci.popen_engine('./stockfish/stockfish-9-64')
        self.engine.uci()
        self.Move = chess.Move

    def random_move(self):
        legalmoves = [move for move in self.board.legal_moves]
        return random.choice(legalmoves)


    def is_move_legal(self,move):
        legalmoves = san_legal_moves(self)
        if move in legalmoves:
            return True
        else:
            return False


    def san_legal_moves(self):
        legalmoves = [self.board.san(move) for move in self.board.legal_moves]
        return legalmoves


    def stockfish_move(self,search=2,thinktime=1000):
        self.engine.position(self.board)
        enginemoves = self.engine.go(movetime=thinktime,depth=search)
        return enginemoves


    def uci_2_move(self,uci):
        return self.Move.from_uci(uci)


