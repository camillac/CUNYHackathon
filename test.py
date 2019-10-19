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

speed = 10

screen_x = 1450
screen_y = 800
boundary_left = 725
boundary_up = -400
boundary_right = -1560
boundary_down = -1200

screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
# set display color as ocean blue
screen.fill((7,176,157))
pygame.display.flip()

### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision
def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join(".", i)).convert_alpha()

turtle = load_image("turtle_right.png")
map = load_image("map.png")
# map = pygame.transform.scale2x(map)
ocean = load_image("ocean.png")
ocean = pygame.transform.scale2x(ocean)

# create a mask for each of them.
turtle_mask = pygame.mask.from_surface(turtle, 50)
map_mask = pygame.mask.from_surface(map, 50)

turtle_rect = turtle.get_rect()
map_rect = map.get_rect()

# a message for if the map hits the terrain.
afont = pygame.font.Font(None, 16)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))
boundr = afont.render("Can't move anymore", 1, (255,255,255))


if screen.get_bitsize() == 8:
    screen.set_palette(ocean.get_palette())
else:
    ocean = ocean.convert()

anim = 0.0

# mainloop
xblocks = range(0, screen_x, 20)
yblocks = range(0, screen_y, 20)

# start the main loop.

map_rect[0] = -100
map_rect[1] = -100

while going:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[QUIT] or keys[K_ESCAPE]:
        going = 0

    # move the map around, depending on the keys.
    if keys[K_LEFT]:
        # print(map_rect.x)
        if map_rect.x + speed <= 0:
            map_rect.x += speed
            turtle = load_image("turtle_left.png")
            turtle_mask = pygame.mask.from_surface(turtle, 50)
    if keys[K_RIGHT]:
        # print(map_rect.x)
        if map_rect.x - speed >= boundary_right:
            map_rect.x -= speed
            turtle = load_image("turtle_right.png")
            turtle_mask = pygame.mask.from_surface(turtle, 50)
    if keys[K_UP]:
        # print(map_rect.y)
        if map_rect.y + speed <= 0:
            map_rect.y += speed
            # turtle = load_image("turtle_up.png")
            # turtle_mask = pygame.mask.from_surface(turtle, 50)
    if keys[K_DOWN]:
        # print(map_rect.y)
        if map_rect.y - speed >= boundary_down:
            map_rect.y -= speed
            # turtle = load_image("turtle_down.png")
            # turtle_mask = pygame.mask.from_surface(turtle, 50)


    # see how far the map rect is offset from the turtle rect.
    bx, by = (map_rect[0], map_rect[1])
    offset_x = bx - math.floor(screen_x/2-150)#turtle_rect[0]
    offset_y = by - math.floor(screen_y/2-100)#turtle_rect[1]

    #print bx, by
    overlap = turtle_mask.overlap(map_mask, (offset_x, offset_y))

    #
    last_bx, last_by = bx, by


    # draw the background color, and the terrain.
    screen.fill((7,176,157))

    # liquid function for making it liquidy
    anim = anim + 0.02
    for x in xblocks:
        xpos = (x + (sin(anim + x * 0.01) * 15)) + 20
        for y in yblocks:
            ypos = (y + (sin(anim + y * 0.01) * 15)) + 20
            screen.blit(ocean, (x, y), (xpos, ypos, 20, 20))

    # see if there was an overlap of pixels between the map
    #   and the terrain.
    if overlap:
        # we have hit the wall!!!  oh noes!
        if keys[K_LEFT]:
            map_rect.x -= speed
        if keys[K_RIGHT]:
            map_rect.x += speed
        if keys[K_UP]:
            map_rect.y -= speed
        if keys[K_DOWN]:
            map_rect.y += speed
        print("COLLISION!")

    # draw map + turtle
    screen.blit(map, (map_rect[0], map_rect[1]) )
    screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center
    # draw the map rect, so you can see where the bounding rect would be.
    pygame.draw.rect(screen, (0,255,0), map_rect, 1)


    # flip the display.
    pygame.display.flip()
    time.sleep(0.01)

    # # limit the frame rate to 40fps.
    # clock.tick(40)

pygame.quit()
