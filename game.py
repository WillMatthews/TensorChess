#!/usr/bin/python3

import chess
import os

clear = lambda: os.system('clear')


def gameloop():
    board = chess.Board()
    prev_illegal = False
    while not board.is_game_over():
        clear()
        print('Chess 0.1')
        if board.turn:
            toplay = "White"
        else:
            toplay = "Black"
        print(toplay + " to play\n\n")

        print(board)

        if prev_illegal:
            print("\nIllegal, enter a new move")
            prev_illegal = False

        mv = input("\nMake your move:  ")

        legalmoves = [board.san(move) for move in board.legal_moves]
        if mv.lower() == "resign":
            return(~ board.turn)
        if mv not in legalmoves:
            prev_illegal = True
        else:
            gamemove = board.parse_san(mv)
            board.push(gamemove)

if __name__ == "__main__":
    winner = gameloop()
    if winner:
        winstr = "White"
    else:
        winstr = "Black"
    print(winstr + " Wins!")
