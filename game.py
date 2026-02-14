import pygame as pg
from enemy import Enemy
from world import World
import constants as c

# Initialize Pygame
pg.init()

# Control FPS
clock = pg.time.Clock()

# Create a game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Orbit Defense")

# Load images
# map
map_img = pg.image.load('Assets/Background/space_background_mcgill.png').convert_alpha()
# enemies
meteor1_img = pg.image.load('Assets/Enemies/meteor1.png').convert_alpha()

# create world
world = World(map_img)

# create groups
enemy_group = pg.sprite.Group()

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

    screen.fill('gray100')

    # draw level
    world.draw(screen)

    # draw enemy path
    pg.draw.lines(screen, 'black', False, waypoints)

    # update groups
    enemy_group.update()

    # draw groups
    enemy_group.draw(screen)

    #event handler
    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            run = False
    # Update the display
    pg.display.flip()
# Quit Pygame
pg.quit()