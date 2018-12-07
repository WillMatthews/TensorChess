# TENSORCHESS
A tensorflow-based zero knowledge chess engine, with an online chess game interface thrown in for free


### Website Structure

##### Current
+ Home
  + Stockfish Survival
  + Stockfish vs Stockfish
  + Random Chess

##### Planned
+ Home
  + Games
    + Multiplayer
    + TensorChess Challenge
    + Stockfish Survival
    + Stockfish vs The World
    + Stockfish vs Stockfish
  + Experiments
    + Random Chess
  + Analysis
    + Game analysis by ID
    + Game analysis by PGN
    + TensorChess Training Stats
    + Website Stats
    + Game browser
    + Download all games


Screenshot of the 'Stockfish Survival' page:
![screenshot](https://github.com/WillMatthews/TensorChess/raw/master/src/common/static/img/screenshot.png "One of the many avaliable modes"



### TODOs

##### UI and Client Mechanics
- [x] Setup a usable interface to the 'chessboard' for a user.
    - [x] Display a live FEN string for the board, for each move.
    - [x] Display a move list.
    - [ ] Display a basic analysis.
    - [x] Display 'pieces in pocket' for each side.
    - [x] Add move sounds.
    - [ ] Add a 'scroll back' method.
    - [ ] Allow user to choose the colour of their game pieces.
- [x] Prettify user interface a bit.
    - [ ] Make navigation bar work properly (currently thinks its always on Home).
    - [x] Make navigation bar collapse properly and not obscure board.
    - [ ] Prettify move list.
    - [ ] Prettify FEN display.
- [ ] Add method for allowing 'takebacks' against Stockfish / other users.
- [ ] Add method for allowing 'resigns' against Stockfish / other users.
- [ ] Add a public, unlogged chat.
- [ ] Setup a very basic game analysis (Use stockfish or similar to analyse positions on-server)
- [ ] Setup an opening practise zone.
- [ ] Setup an endgame practise zone.
- [ ] Add a 'load from FEN' mode.

##### Server Mechanics
- [ ] Add a 'Common' websocket communication protocol.
    - [x] Push moves to client with WebSockets (and return moves).
    - [x] Allow user to play against Stockfish.
    - [ ] Log game moves to a database.
    - [ ] Log high scores (for stockfish survival) (number of moves / if you win).
        - [ ] Show a 'high scores' list on server.
- [ ] Add a 'log in' method?
- [ ] Identify well-played games and assign a score to it for how interesting the game is. 

##### Game Modes
- [ ] Add support for multiple users, rather than single session (related to common comms socket).
- [ ] Allow player-to-player games.
    - [ ] Add a chat application on the websocket communication network (do not log to DB for privacy).
- [ ] Add a 'Stockfish vs The World' game mode.

##### Support
- [ ] Add a feedback section for users to tell me what's not so great, and allow bug reports.
- [ ] Allow for the boards to be resettable, and add a generic board that takes arguments of the game type so making new boards is not necessary.

##### Engines
- [ ] Implement a simple minmax algorithm.
- [ ] Try to make minmax good enough to beat a human.
- [ ] Make TensorChess work!
    - [ ] Define a suitable feature vector for the board state.
    - [ ] Start work on zero knowledge ML for this chess application.
    - [ ] Try to make ML beat this minmax.
    - [ ] Consider some learned chess ML as well?


**_Established on the 10th anniversary of Stockfish_**
