import chess
import chess.svg
import os

clear = lambda: os.system('clear')

class State(object):
    def __init__(self,board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board


    def gameloop(self):
        prev_illegal = False
        while not self.board.is_game_over():
            clear()
            print('Chess 0.1')
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

    def showpiece(self):
        """Generate SVG graphics for the flask app??"""

