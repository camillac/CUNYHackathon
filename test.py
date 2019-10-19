import os
import pygame
import math
from math import sin
from pygame.locals import *
import time

main_dir = os.path.split(os.path.abspath(__file__))[0]

pygame.display.init()
pygame.font.init()

logo = pygame.image.load("turtle_left.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Turtles In Trash")

going = 1

screen_x = 1450
screen_y = 800
screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
# set display color as ocean blue
screen.fill((7,176,157))
pygame.display.flip()

### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision
def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join(".", i)).convert_alpha()

turtle = load_image("turtle_right.png")
trash = load_image("map.png")
ocean = load_image("ocean.jpg")
ocean = pygame.transform.scale2x(ocean)

# create a mask for each of them.
turtle_mask = pygame.mask.from_surface(turtle, 50)
trash_mask = pygame.mask.from_surface(trash, 50)

turtle_rect = turtle.get_rect()
trash_rect = trash.get_rect()

# a message for if the balloon hits the terrain.
afont = pygame.font.Font(None, 16)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))

if screen.get_bitsize() == 8:
    screen.set_palette(ocean.get_palette())
else:
    ocean = ocean.convert()

anim = 0.0

# mainloop
xblocks = range(0, screen_x, 20)
yblocks = range(0, screen_y, 20)

# start the main loop.

while going:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[QUIT] or keys[K_ESCAPE]:
        going = 0
    # if e.type == pygame.KEYDOWN:
    #     # move the balloon around, depending on the keys.
    if keys[K_LEFT]:
        trash_rect.x += 3
        turtle = load_image("turtle_left.png")
    if keys[K_RIGHT]:
        trash_rect.x -= 3
        turtle = load_image("turtle_right.png")

    if keys[K_UP]:
        trash_rect.y += 3
    if keys[K_DOWN]:
        trash_rect.y -= 3

    # see how far the balloon rect is offset from the terrain rect.
    bx, by = (trash_rect[0], trash_rect[1])
    offset_x = bx - math.floor(screen_x/2-150)#turtle_rect[0]
    offset_y = by - math.floor(screen_y/2-100)#turtle_rect[1]

    #print bx, by
    overlap = turtle_mask.overlap(trash_mask, (offset_x, offset_y))

    #
    last_bx, last_by = bx, by


    # draw the background color, and the terrain.
    screen.fill((7,176,157))

    # liquid function for making it liquidy
    anim = anim + 0.1
    for x in xblocks:
        xpos = (x + (sin(anim + x * 0.01) * 15)) + 20
        for y in yblocks:
            ypos = (y + (sin(anim + y * 0.01) * 15)) + 20
            screen.blit(ocean, (x, y), (xpos, ypos, 20, 20))

    # draw trash + turtle
    screen.blit(trash, (trash_rect[0], trash_rect[1]) )
    screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center
    # draw the balloon rect, so you can see where the bounding rect would be.
    pygame.draw.rect(screen, (0,255,0), trash_rect, 1)


    # see if there was an overlap of pixels between the balloon
    #   and the terrain.
    if overlap:
        # we have hit the wall!!!  oh noes!
        screen.blit(hitsurf, (0,0))

    # flip the display.
    pygame.display.flip()
    time.sleep(0.01)

    # # limit the frame rate to 40fps.
    # clock.tick(40)



pygame.quit()
