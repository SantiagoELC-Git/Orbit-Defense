import pygame as pg

class Turret(pg.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.range = 90
        self.selected = False

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # transparent circle for range
        self.range_image = pg.Surface((self.range*2, self.range*2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, 'grey10', (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
    
    def draw (self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
