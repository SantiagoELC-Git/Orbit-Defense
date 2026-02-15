import pygame as pg
from enemyREAL import Enemy, Planet
from world import World
from turret import Turret
from buttons import Button
import constants as c
from world import World
import json
import constants as c


# Initialize Pygame
pg.init()

# Setting up the Screen
background_width = c.SCREEN_WIDTH + c.SIDE_PANEL
background_height = c.SCREEN_HEIGHT
screen = pg.display.set_mode((background_width, background_height))
pg.display.set_caption("Orbit Defense")

# game stuff
placing_turrets = False
selected_turret = None

# Images 

# Load and rescale the background image
space_background = pg.image.load('Pixel-Art/Background/space.png')
scal_space_background = pg.transform.scale(space_background, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT)).convert()
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
world = World(world_data, space_background)
world.process_data()

# create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

# create buttons
heisenberg_button = Button(c.SCREEN_WIDTH + 100, 50, buy_heisenberg_img) 
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_button_img) 

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
    turret_group.update(enemy_group)

    # highlighting slected turret
    if selected_turret:
        selected_turret.selected = True


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
            running = False
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

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pg.quit()
