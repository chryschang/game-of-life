# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:05:48 2016

@author: apgt
"""
import numpy as np

#Creating the grid
grid = np.zeros(10000).reshape(100,100)

#Initial Pattern



#Game

#Takes as input the coordinates (x,y) and returns the sum of the neighbors
def neighbors(posh,posv):
    rot=[-1,0,1]
    num_living_cells=0
    for i in range(3):
        for j in range(3):
            num_living_cells+=grid[posv+rot[j],posh+rot[i]]
    return num_living_cells-grid[posv,posh]




#Print grid
