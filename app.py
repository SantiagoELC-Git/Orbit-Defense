import pygame as pg

# Initialize Pygame
pg.init()

# Setting screen dimensions
Screen_dim = (1220, 675)

# Setting up the Screen
screen = pg.display.set_mode(Screen_dim)


# Images 
# Load and rescale the background image
space_background = pg.image.load('Pixel-Art/space.png')
scal_space_background = pg.transform.scale(space_background, Screen_dim).convert()
# Earth
earth = pg.image.load('Pixel-Art/Earth.png')
scal_earth = pg.transform.scale(earth,(200,200))



running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Draw background
    screen.blit(scal_space_background, (0, 0))

    # Draw the Earth
    screen.blit(scal_earth, (1025, 500))

    # Update the display
    pg.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

# Quit Pygame
pg.quit()
