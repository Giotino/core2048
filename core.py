'''
Created on 16/mag/2014

@author: Giotino
'''

import random        

class game_istance(object):
    
    def __init__(self, serie, size, direct_name):
        self.direct_name = direct_name
        self.serie = serie
        self.size = size
        self.lost = False
        self.grid = [[0 for x in xrange(size)] for x in xrange(size)]
        self.old_grids = []
        self.start()
        
    def start(self):
        pass
        
    def spawn(self):
        if random.randint(1, 10) == 1:
            self.lastspawn = self.serie[1]
        else:
            self.lastspawn = self.serie[0]
        cells = self.freecells(self.grid)
        if len(cells) > 1:
            rndfreecell = cells[random.randint(0, len(cells)-1)]
            self.setcell(rndfreecell[0], rndfreecell[1], self.lastspawn)
        else:
            for move in self.direct_name:
                new_grid = self.sim_move(move)
                if new_grid != self.grid:
                    continue
                elif move == self.direct_name[3]:
                    self.lost = True
    
    def setcell(self, row, col, num):
        self.grid[row][col] = self.serie[num]
            
    def freecells(self, grid):
        return self.search(grid, -1, -1)
            
    def search(self, grid, num, many):
        found = []
        if num == -1:
            num = 0
        else:
            num = self.serie[num]
        for nrow, row in enumerate(grid):
            if many == 0:
                break
            for ncol, col in enumerate(row):
                if many == 0:
                    break
                if col == num:
                    found.append([nrow, ncol])
                    many -= 1
        return found
                        
    def move(self, direct):
        self.old_grids.append(self.grid)
        
        if direct == self.direct_name[0]:
            self.grid = self.move_updown(False)
        elif direct == self.direct_name[1]:
            self.grid = self.move_updown(True)
        elif direct == self.direct_name[2]:
            self.grid = self.move_leftright(False)
        elif direct == self.direct_name[3]:
            self.grid = self.move_leftright(True)
        else:
            return None
        
    def sim_move(self, direct):
        if direct == self.direct_name[0]:
            return self.move_updown(False)
        elif direct == self.direct_name[1]:
            return self.move_updown(True)
        elif direct == self.direct_name[2]:
            return self.move_leftright(False)
        elif direct == self.direct_name[3]:
            return self.move_leftright(True)
        else:
            return None
        
    def move_updown(self, top):
        r = range(self.size-1, -1, -1) if top else range(self.size)
        grid = self.grid
        grid_tmp = grid
        
        for iy in range(self.size):
            # get all the cube for the current line
            cubes = []
            for ix in r:
                cube = grid[ix][iy]
                if cube != 0:
                    cubes.append(cube)
            # combine them
            cubes = self.combine(cubes)

            # update the grid
            for ix in r:
                cube = cubes.pop(0) if cubes else 0
                if grid_tmp[ix][iy] != cube:
                    self.moved = True
                grid_tmp[ix][iy] = cube
                if not cube:
                    continue
        return grid_tmp

    def move_leftright(self, right):
        r = range(self.size-1, -1, -1) if right else range(self.size)
        grid = self.grid
        grid_tmp = grid
        
        for ix in range(self.size):
            # get all the cube for the current line
            cubes = []
            for iy in r:
                cube = grid[ix][iy]
                if cube != 0:
                    cubes.append(cube)

            # combine them
            cubes = self.combine(cubes)

            # update the grid
            for iy in r:
                cube = cubes.pop(0) if cubes else 0
                if grid_tmp[ix][iy] != cube:
                    self.moved = True
                grid_tmp[ix][iy] = cube
                if not cube:
                    continue
        return grid_tmp
                
    def combine(self, cubes):
        if len(cubes) <= 1:
            return cubes
        else:
            self.moved = False
        index = 0
        while index < len(cubes) - 1:
            cube1 = cubes[index]
            cube2 = cubes[index + 1]
            if cube1 == cube2:
                cube1 = self.serie[self.serie.index(cube1)+1]
                del cubes[index + 1]
                cubes[index] = cube1
            index += 1
        return cubes
        
if __name__ == '__main__':
    pass
    #currgame = game_istance([pow(2, x) for x in range(20)], 4, [0, 1, 2, 3])