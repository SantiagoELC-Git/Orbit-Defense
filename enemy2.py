import pygame as pg
from pygame import Vector2
import math

class Enemy(pg.sprite.Sprite):
    # constants 
    AU = 1       # AU in meters
    G =  6.67e-11    # gravitational constant
    TIMESTEP = 1    # 1 day per update in seconds
    SCALE = 1        # 1 pixel = 1e9 meters


    def __init__(self, waypoints, image, mass):
        "Initialize enemy sprite"
        pg.sprite.Sprite.__init__(self)
        self.mass = mass
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                        # rotation?
        self.vel = Vector2(0,1)                         # starting velocity 
        self.speed = 2                                  # optional?
        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def attraction(self, other):
        "Calculate gravitational force from another object"
        direction = Vector2(other.x, other.y) - self.pos            # vector pointing toward other 
        distance = direction.length()
        if distance == 0:                                           # avoid division by zero
            return Vector2(0,0)
        force_mag = self.G * self.mass * other.mass / distance**2   # magnitude of force
        force = direction.normalize() * force_mag                   # convert to vector 
        return force
    
    def update(self, celestial_objects = None):
        "Update enemy position, velocity, waypoints, and rotation based on gravitational force."
        if celestial_objects is None:
            celestial_objects = [] 
        total_force = Vector2(0, 0)
        
        # sum gravitational forces from all other celestial objects
        for obj in celestial_objects:
            if obj == self:
                continue
            total_force += self.attraction(obj)
        
        # convert net force to acceleration: a = F/m
        acceleration = total_force / self.mass
        
        # update velocity in m/s and position in meters
        self.vel += acceleration * self.TIMESTEP
        pos_meters = self.pos * self.SCALE
        pos_meters += self.vel *self.TIMESTEP

        # convert back to pixel
        self.pos = pos_meters / self.SCALE
        
        # record current position as a dynamic waypoint
        self.waypoints.append(Vector2(self.pos))
        
        # optional: trim waypoints to limit trail length
        # MAX_TRAIL_LENGTH = 500
        # if len(self.waypoints) > MAX_TRAIL_LENGTH:
        #    self.waypoints.pop(0)
        
        self.move()
        self.rotate()

    def move(self):
        # define the target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
            if self.movement.length() != 0:
                self.pos += self.vel
                # incerement target waypoint when close enough
                if self.movement.length() < self.vel.length():
                    self.target_waypoint += 1
        else:
            # enemy has reached the end of the path, so we remove it from the game
            self.kill()

    def rotate(self):
        # calculate distance to next waypoint
        if self.target_waypoint < len(self.waypoints):
            dist = self.waypoints[self.target_waypoint] - self.pos
            # use distance to calculate angle
            self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
            # rotate image and update rectangle
            self.image = pg.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass                # in kg
