import chess
import chess.svg
import chess.uci
import os

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

    def gameloop(self):
        prev_illegal = False
        while not self.board.is_game_over():
            clear()
            print('TensorChess 0.1')
            if self.board.turn:
                toplay = "White"
            else:
                toplay = "Black"
            print(toplay + " to play\n\n")

            print(self.board)

            if prev_illegal:
                print("\nIllegal, enter a new move")
                prev_illegal = False

            mv = input("\nMake your move:  ")

            legalmoves = [self.board.san(move) for move in self.board.legal_moves]
            if mv.lower() == "resign":
                return(~ self.board.turn)
            if mv not in legalmoves:
                prev_illegal = True
            else:
                gamemove = self.board.parse_san(mv)
                self.board.push(gamemove)

    def san_legal_moves(self):
        legalmoves = [self.board.san(move) for move in self.board.legal_moves]
        return legalmoves

    def engine_move(self):
        self.engine.position(self.board)
        enginemoves = self.engine.go(depth=2)
        return enginemoves

    def uci_2_move(self,uci):
        return self.Move.from_uci(uci)

