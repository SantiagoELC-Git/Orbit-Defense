import numpy as np
import pygame as  pg
import math
from enemy import Enemy

class Enemy(pg.sprite.Sprite):
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 pixel
    TIMESTEP = 3600*24 # 1 day
    def __init__ (self, x, y, radius, image, mass):
        self.x = x                              # position on screen 
        self.y = y
        self.radius = radius
        self.image = []
        self.mass = mass
        self.orbit = []
        self.planet  = False
        self.distance_to_planet = 0
        self.x_vel = 0
        self.y_vel = 0

def main():
    run = True
    clock = pg.time.Clock()
    planet = Enemy(0, 0, 30, Earth.png ) # radius is in 30
