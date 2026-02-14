import pygame as pg
from enemy2 import Enemy, Planet
from world import World
from turret import Turret
from buttons import Button
import constants as c
from enemyREAL import Enemy, Planet
from world import World


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
# individual turrent image under cursor
cursor_turret1 = pg.image.load('Pixel-Art/Turrets/turret_placeholder.png').convert_alpha()
# enemies
meteor1_img = pg.image.load('Pixel-Art/Enemies/meteor1.png').convert_alpha()
# buttons


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

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    # Calculate the sequential tile number
    #mouse_tile_num = 
    turret = Turret(cursor_turret1, mouse_pos)
    turret_group.add(turret)


# create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()


planetNeptune = Planet(175, 175, mass=600)
planetUranus = Planet(275, 325, mass=600)
planetSaturn = Planet(375, 475, mass = 900)
planetJupiter = Planet(600, 250, mass = 1000)
planetMars = Planet(700, 450, mass=300)
planetEarth = Planet(875, 575, mass = 3000)

celestial_objects = [planetEarth, planetNeptune, planetUranus, planetSaturn, planetJupiter, planetMars]

waypoints = [
    (40, 40)
]

meteor1 = Enemy(waypoints, meteor1_img, 50)
enemy_group.add(meteor1)

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Draw background
    screen.blit(scal_space_background, (0, 0))

    clock.tick(c.FPS) # Set the frame rate to 60 

    #####
    # Updating
    #####

    # update groups
    enemy_group.update(celestial_objects)

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

    pg.draw.lines(screen, 'black', False, waypoints)

    # draw groups
    enemy_group.draw(screen)
    turret_group.draw(screen)


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

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pg.quit()
