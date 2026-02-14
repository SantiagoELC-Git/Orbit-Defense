import pygame as pg
import json
from enemy import Enemy
from world import World
from turret import Turret
from buttons import Button
import constants as c

# Initialize Pygame
pg.init()

# Control FPS
clock = pg.time.Clock()

# Create a game window
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Orbit Defense")

# game stuff
placing_turrets = False
selected_turret = None

# Load images
# map
map_img = pg.image.load('Pixel-Art/Background/full_background.png').convert_alpha()
# individual turrent image under cursor
cursor_turret1 = pg.image.load('Pixel-Art/Turrets/turret_placeholder.png').convert_alpha()
# enemies
meteor1_img = pg.image.load('Pixel-Art/Enemies/meteor1.png').convert_alpha()
# buttons
buy_heisenberg_img = pg.image.load('Pixel-Art/Buttons/HEISENBERG.png').convert_alpha()
cancel_button_img = pg.image.load('Pixel-Art/Buttons/Cancel_Button.png').convert_alpha()

# load json data for level
with open('Pixel-Art/Background/placeable_area.tmj') as file:
    world_data = json.load(file)


def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    # Calculate the sequential tile number
    mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
    # check if that tile is placeable or not
    if world.tile_map[mouse_tile_num] != 0:
        # check that there isn't already a turret there
        space_is_free = True
        for turret in turret_group:
            if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
                space_is_free = False
        # if the space is free, create a turret there
        if space_is_free == True:
            turret = Turret(cursor_turret1, mouse_tile_x, mouse_tile_y)
            turret_group.add(turret)

def select_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    for turret in turret_group:
        if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
            return turret

def clear_selection():
    for turret in turret_group:
        turret.selected = False

# create world
world = World(world_data, map_img)
world.process_data()

# create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

# create buttons
heisenberg_button = Button(c.SCREEN_WIDTH + 100, 50, buy_heisenberg_img) 
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_button_img) 


waypoints = [
    (100, 200),
    (300, 100),
    (400, 400),
    (67, 67)
]

meteor1 = Enemy(waypoints, meteor1_img)
enemy_group.add(meteor1)

# Makes game run
run = True
while run:

    clock.tick(c.FPS) # Set the frame rate to 60 

    #####
    # Updating
    #####

    # update groups
    enemy_group.update()
    turret_group.update()

    # highlighting slected turret
    if selected_turret:
        selected_turret.selected = True
    
    print(turret_group)

    #####
    # Drawing
    #####

    screen.fill('gray100')

    # draw level
    world.draw(screen)

    # draw enemy path
    pg.draw.lines(screen, 'black', False, waypoints)

    # draw groups
    enemy_group.draw(screen)
    for turret in turret_group:
        turret.draw(screen)

    # draw buttons
    # button for placing turrets
    if heisenberg_button.draw(screen):
        placing_turrets = True
    # if placing turrets, show the cancel button
    if placing_turrets == True:
        # shower turret under cursor
        cursor_rect = cursor_turret1.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] < c.SCREEN_WIDTH:
            screen.blit(cursor_turret1, cursor_rect)
        if cancel_button.draw(screen):
            placing_turrets = False

    #event handler
    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            run = False
        # mouse click
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            # check if mouse is within bounds of the screen
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                # clear selected turret if you click within play area
                selected_turret = None
                clear_selection()
                if placing_turrets == True:
                    create_turret(mouse_pos)
                else:
                    selected_turret = select_turret(mouse_pos)

    # Update the display
    pg.display.flip()
# Quit Pygame
pg.quit()