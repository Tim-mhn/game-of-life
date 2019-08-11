# Game of Life

The game of life is not an actual game but a cellular automaton. An initial grid of black and white cells determines how the grid will evolve following very basic rules. Live cells are black, dead cellsare white here. The 8 cells surrounding each cells are called its neighbours.

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

GUI developed using the python library Tkinter that allows one to set an initial state and observe its evolution.
