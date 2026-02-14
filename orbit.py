import numpy as np
import pygame as  pg
import math
from enemy import Enemy

class Enemy():
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
    def attraction(self, other):                    # implement the physics where other is the celestial objects
        other_x, other_y = other.x, other.y 
        # calculate distance between two objects
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # determine if the other object is the solar system planets
        if other.planet:
            self.distance_to_planet = distance

        # calculate the force of attraction  F = GMm/r^2
        force = self.G * self.mass * other.mass * self.radius / distance**2
        theta = math.atan2(distance_y/distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin (theta) * force
        return force_x, force_y
    
    def update_position(self, enemies):
        total_fx = total_fy = 0
        for enemy in enemies:
            if self == enemy:
                continue
            fx, fy = self.attraction(enemy)
            total_fx += fx
            total_fy += fy
        self.x_vel = total_fx/self.mass * self.TIMESTEP

        F = m/a
        a = f/m
        