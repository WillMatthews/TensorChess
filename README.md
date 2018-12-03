# TENSORCHESS
A tensorflow-based zero knowledge chess engine and online chess game interface


### Website Structure

+ Index
  + Multiplayer
  + TensorChess Challenge
  + Stockfish Survival
  + Random Chess

### TODOs

- [x] Setup a usable interface to the 'chessboard' for a user.
    - [ ] Display a live FEN string for the board, for each move.
    - [ ] Display a move list.
    - [ ] Display a basic analysis.
- [x] Push moves to client with WebSockets (and return moves).
    - [ ] Add a 'Common' websocket communication protocol.
- [x] Allow user to play against Stockfish.
    - [ ] Add method for allowing 'takebacks' against Stockfish.
    - [ ] Log game moves.
    - [ ] Log high scores (number of moves / if you win).

- [ ] Add a feedback section for users to tell me what's not so great, and allow bug reports.
- [ ] Add support for multi player rather than single session.
- [ ] Allow player-to-player games.
    - [ ] Add a chat application on the websocket communication network (do not log to DB for privacy).
- [x] Prettify user interface a bit.
    - [ ] Make navigation bar work properly (currently thinks its always on Home)
    - [x] Make navigation bar collapse properly and not obscure board

- [ ] Allow for the boards to be resettable, and add a generic board that takes arguments of the game type so making new boards is not necessary.

- [ ] Setup a very basic game analysis (Use stockfish or similar to analyse positions on-server)
- [ ] Setup an opening practise zone.
- [ ] Setup an endgame practise zone.
- [ ] Add a 'load from FEN' mode.

- [ ] Implement a simple minmax algorithm.
- [ ] Try to make minmax good enough to beat a human.

- [ ] Define a suitable feature vector for the board state.
- [ ] Start work on zero knowledge ML for this chess application.
- [ ] Try to make ML beat this minmax.
- [ ] Consider some learned chess ML as well?



Established on the 10th anniversary of Stockfish
