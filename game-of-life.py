# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:05:48 2016

@author: apgt
"""
import numpy as np
import time
from random import randint

# timer to see how long it takes
start_time = time.clock()

#initial frame size. shrunk it for testing
n_row = 10
n_col = 10
zeros = n_row * n_col

#Creating the grid
grid = np.zeros(zeros).reshape(n_row, n_col)

# Populate the grid randomly
def randgrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            grid[x,y] = randint(0,1)

# Blinker test case. Three values in a row flips to three in a column and vice versa.
def blinker(grid):
    for x in range(2, 5):
        for y in range(4,5):
            grid[x, y] = 1

#Takes as input the coordinates (x,y) and returns the sum of the neighbors
def neighbors(posh,posv):
    rot=[-1,0,1]
    num_living_cells=0
    for i in range(3):
        for j in range(3):
            ver = posv+rot[j]
            hor = posh+rot[i]
            if ver < n_row and ver >= 0 and hor < n_col and hor >= 0:
                num_living_cells += grid[ver, hor]
    return num_living_cells-grid[posv,posh]

#Apply the rules
def tick(Grid):
    ncount = 0
    temp = np.zeros(zeroes).reshape(n_row, n_col)
    for x in range(len(Grid)):
        for y in range(len(Grid)):
            ncount = neighbors(y,x)
            # rules 1-3
            if Grid[x, y] == 1:
                if ncount < 2 or ncount > 3:
                    temp[x, y] = 0
                else:
                    temp[x, y] = Grid[x, y]
            # rule 4
            if Grid[x, y] == 0:
                if ncount == 3:
                    temp[x, y] = 1
                else:
                    temp[x, y] = Grid[x, y]
    return temp

# Grid printer
def show(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x,y] == 1:
                print('\x1b[0;36;42m 1 \x1b[0m', end = "")
            else:
                print(" 0 ", end = "")
            if y == len(grid)-1:
                print("\n")
                
#randgrid(grid) #Initialize the grid
blinker(grid) #Initialize the grid with a blinker pattern
print("Init")
show(grid) # Generation 0
for i in range(3):
    grid = tick(grid)
    print("Tick")
    show(grid)
                
print("---%s seconds---" % (time.clock() - start_time))
