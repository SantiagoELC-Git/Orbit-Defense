import pygame as pg

class World():
    def __init__(self, data, map_img):
        self.tile_map = []
        self.level_data = data
        self.image = map_img

    def process_data(self):
        # look through the data and take whatever is needed/useful
        for layer in self.level_data["layers"]:
            print(layer["name"])
        if layer["type"] == "tilelayer":
            self.tile_map = layer["data"]
            print(self.tile_map)
    
    def draw(self, surface):
        surface.blit(self.image, (0, 0))