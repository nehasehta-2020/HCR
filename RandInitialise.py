# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:47:22 2023

@author: LENOVO
"""

import numpy as np
 
def initialise(a, b):
    epsilon = 0.15
    c = np.random.rand(a, b + 1) * (
      # Randomly initialises values of thetas between [-epsilon, +epsilon]
      2 * epsilon) - epsilon 
    return c