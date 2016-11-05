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

#Game

#Takes as input the coordinates (x,y) and returns the sum of the neighbors
def neighbors(posh,posv):
    rot=[-1,0,1]
    num_living_cells=0
    for i in range(3):
        for j in range(3):
            if posv+rot[j] < len(grid) and posv+rot[j] >= 0 and posh+rot[i] < len(grid) and posh+rot[i] >= 0:
                num_living_cells+=grid[posv+rot[j],posh+rot[i]]
    return num_living_cells-grid[posv,posh]

#Apply the rules
def tick(grid):
    ncount = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            ncount = neighbors(x,y)
            #rules 1-3
            if grid[x,y] == 1:
                if ncount < 2 or ncount > 3:
                    grid[x,y] = 0
            #rule 4
            if grid[x,y] == 0:
                if ncount == 3:
                    grid[x,y] = 1

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
                
randgrid(grid) #Initialize the grid
show(grid) # Generation 0
tick(grid) #Apply the rules
show(grid) # Generation 1
                
print("---%s seconds---" % (time.clock() - start_time))
