__author__ = 'luca.piccinelli'
import random
import numpy as np
import pygame
from pygame import surfarray

class Matrix:
    def __init__(self):
        self.data = np.array([random.randrange(255) for i in range(0, 10000)]).reshape(100, 100)

    def to_surface(self):
       return surfarray.make_surface(self.data)
