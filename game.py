import pygame as pg
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

# Load images
# map
map_img = pg.image.load('Pixel-Art/Background/space.png').convert_alpha()
# individual turrent image under cursor
cursor_turret1 = pg.image.load('Pixel-Art/Turrets/turret_placeholder.png').convert_alpha()
# enemies
meteor1_img = pg.image.load('Pixel-Art/Enemies/meteor1.png').convert_alpha()
# buttons
buy_heisenberg_img = pg.image.load('Pixel-Art/Buttons/HEISENBERG.png').convert_alpha()
cancel_button_img = pg.image.load('Pixel-Art/Buttons/Cancel_Button.png').convert_alpha()

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    # Calculate the sequential tile number
    #mouse_tile_num = 
    turret = Turret(cursor_turret1, mouse_pos)
    turret_group.add(turret)

# create world
world = World(map_img)

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
    turret_group.draw(screen)

    # draw buttons
    # button for placing turrets
    if heisenberg_button.draw(screen):
        print ("heisenberg button clicked")
    if cancel_button.draw(screen):
        print("cancel button clicked")

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
                create_turret(mouse_pos)

    # Update the display
    pg.display.flip()
# Quit Pygame
pg.quit()