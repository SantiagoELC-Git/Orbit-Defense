import pygame as pg

class World():
    def __init__(self, map_img):
        self.image = map_img
    
    def draw(self, surface):
        surface.blit(self.image, (0, 0))