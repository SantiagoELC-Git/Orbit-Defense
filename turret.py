import pygame as pg
import constants as c
import math

class Turret(pg.sprite.Sprite):
    def __init__(self, sprite_sheet, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.cooldown = 1500
        self.last_shot = pg.time.get_ticks()

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE

        # animation variables
        self.sprite_sheet = sprite_sheet
        self.animation_list = self.load_images()
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

        self.range = 90
        self.selected = False

        # update img
        self.image = self.animation_list[self.frame_index]
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
    
    def load_images(self):
        # extract imgs from spreadsheet
        size = self.sprite_sheet.get_height()
        animation_list = []
        for x in range(c.ANIMATION_STEPS):
            temp_img = self.sprite_sheet.subsurface(x*size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list


    def draw (self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)

    def update(self, enemy_group):
        # if target picked, play firing animation
        if self.target:
            self.play_animation()
        else:
            # search for new target once turret has cooled down
            if pg.time.get_ticks() - self.last_shot > self.cooldown:
                self.pick_target(enemy_group)

    def pick_target(self, enermy_group):
        # find an enemy to target
        x_dist = 0
        y_dist = 0
        # check distance to each enemy to see if it's in range
        for enemy in enermy_group:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = math.sqrt(x_dist**2 + y_dist**2)
            if dist < self.range:
                self.target = enemy
                print('target acquired')

    def play_animation(self):
        # update img
        self.image = self.animation_list[self.frame_index]
        # check if enough time has passed since last update
        if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1
            # check is animation has finished and reset
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
                # record completed time and clear to start cooldown
                self.last_shot = pg.time.get_ticks()
                self.target = None

