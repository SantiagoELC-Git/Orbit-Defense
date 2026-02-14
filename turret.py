import pygame as pg
import constants as c
import math

class Turret(pg.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE

        self.range = 90
        self.selected = False

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.target = None

        # transparent circle for range
        self.range_image = pg.Surface((self.range*2, self.range*2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, 'grey100', (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
    
    def draw (self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    #def update(enemy_group):


    def pick_target(self, enermy_group):
        # find an enemy to target
        x_dist = 0
        y_dist = 0
        # check distance to each enemy to see if it's in range
        for enemy in enermy_group:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = math.sqrt(x_dist**2 + y_dist**2)
            if dist <= self.range:
                self.target = enemy

