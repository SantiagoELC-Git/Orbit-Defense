import pygame as pg
from enemy import Enemy
from world import World
from turret import Turret
from buttons import Button
import constants as c
from enemyREAL import Enemy, Planet


# Initialize Pygame
pg.init()

# Setting screen dimensions
Screen_dim = (900, 600)

# Setting up the Screen
screen = pg.display.set_mode(Screen_dim)

# Images 

# Load and rescale the background image
space_background = pg.image.load('Pixel-Art/Background/space.png')
scal_space_background = pg.transform.scale(space_background, Screen_dim).convert()

# Earth
earth = pg.image.load('Pixel-Art/Background/Earth.png')
scal_earth = pg.transform.scale(earth,(150,150))

# Pluto 
pluto = pg.image.load("Pixel-Art/Background/Pluto.png")
scal_pluto = pg.transform.scale(pluto, (60,60))

# Jupiter 
Jupiter = pg.image.load("Pixel-Art/Background/Jupiter.png")
scal_Jupiter = pg.transform.scale(Jupiter,(200,200))

# Mars 
Mars = pg.image.load("Pixel-Art/Background/Mars.png")
scal_mars = pg.transform.scale(Mars,(100,100))

# Uranus 
Uranus = pg.image.load("Pixel-Art/Background/Uranus.png")
scal_uranus = pg.transform.scale(Uranus, (150,150))

# Saturn
Saturn = pg.image.load("Pixel-Art/Background/Saturn.png")
scal_Saturn = pg.transform.scale(Saturn, (150, 150))

# Neptune 
Neptune = pg.image.load("Pixel-Art/Background/Neptune.png")
scal_Neptune = pg.transform.scale(Neptune,(150,150))

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Draw background
    screen.blit(scal_space_background, (0, 0))

    # Draw the Earth
    screen.blit(scal_earth, (800, 500))

    # Drawing Pluto
    screen.blit(scal_pluto, (50,25))

    # Drawing Jupiter
    screen.blit(scal_Jupiter, (500,150))

    # Drawing Mars
    screen.blit(scal_mars, (650,400))

    # Drawing Uranus 
    screen.blit(scal_uranus, (200,250))

    # Drawing Saturn
    screen.blit(scal_Saturn, (300,400))

    # Drawing Neptune
    screen.blit(scal_Neptune, (100,100))

    # Update the display
    pg.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pg.quit()
