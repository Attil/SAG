# An example SPADE program.
 This Python project can be used as a point of reference how to use SPADE for Python.

 It calculates probabilities of selected Poker hands. One hand is one agent.

 It assumes you are playing Hold'em, so it'll assume a total end value of 7 cards (5 on the board, 2 in hand).

# Prerequisites
* Python 2.7
* SPADE

# Running
* `configure.py localhost`
* `runspade.py`
* `python solvers.py`
* `python coordinator.py heart:3 spade:5 diamond:2` or whatever

If you don't provide an argument for coordinator, example value of `spade:2 diamond:j heart:k heart:q` will be used.
