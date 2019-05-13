# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:58:27 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

#x = np.linspace(0,10,11)
def funktion(x):
    if x <= m.sqrt(2):
        f = -(x-m.sqrt(2))**2
    else:
        f = (x-m.sqrt(2))**2
    return f


print("Dette er funktionsværdien {:.5f}".format(funktion(3)))