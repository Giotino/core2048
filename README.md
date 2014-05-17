2048 Core
========
This python project is a library for develop 2048 game based and 2048 analysis.

In this library you find a class named game_istance which requires serie output array (example [2, 4, 8, 16, 32]), size of grid side (example 4) and direction name in the order of the example (example ['up', 'down', 'left', 'right']) that are used in move and sim_move function

The function of the class are:
- spawn() - Spawn a tile randomly, the tile chance are 90% serie[0], 10% serie[1]
- setcell(row, col, num) - Change grid[row, col] value to serie[num]
- freecells(grid) - Return array of coordinates of the blank cells of grid
- search(grid, num, many) - Return array[many] of coordinates of the cells that contain serie[num] value
- move(direct) - Move the tiles to 'direct' direction, direct take only value that are into serie[]
- sim_move(direct) - Same function of move(direct) but this doesn't affect the game_instance.grid, it returns the new grid

The global variables of the class are:
- grid - Contains the grid
- lost - Contains the lost status
- old_grids - Contains the grids before the moves
