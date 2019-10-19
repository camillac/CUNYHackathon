import os
import pygame
import math
from pygame.locals import *

pygame.display.init()
pygame.font.init()

pygame.display.set_caption("Turtles In Trash")

going = 1

screen_x = 1450
screen_y = 800
screen = pygame.display.set_mode((screen_x,screen_y)) #sets the display screen

# set display color as ocean blue
screen.fill((7,176,157))
pygame.display.flip() #Update the full display Surface to the screen

### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision
def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join("..", i)).convert_alpha()

turtle = load_image("turtle.png")
trash = load_image("terrain1.png")

# create a mask for each of them.
turtle_mask = pygame.mask.from_surface(turtle, 50)
trash_mask = pygame.mask.from_surface(trash, 50)

turtle_rect = turtle.get_rect() #get rectangualr area from turtle
trash_rect = trash.get_rect() #get rectangular area from the map

# a message for if the balloon hits the terrain.
afont = pygame.font.Font(None, 30)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))


# start the main loop.

while going:
    pygame.event.pump() #handles internal interactions
    keys = pygame.key.get_pressed()
    if keys[QUIT] or keys[K_ESCAPE]:
        going = 0
    # if e.type == pygame.KEYDOWN:
    #     # move the balloon around, depending on the keys.
    if keys[K_LEFT]:
        trash_rect.x += 3
        # turtle = load_image("turtle2.png")
    if keys[K_RIGHT]:
        trash_rect.x -= 3

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
    # screen.blit(turtle, (0,0)) #draws the turtle at the upper right.


    # draw the balloon.
    screen.blit(trash, (trash_rect[0], trash_rect[1]) )
    screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center


    # draw the map rect, so you can see where the bounding rect would be.
    pygame.draw.rect(screen, (0,255,0), trash_rect, 1)


    # see if there was an overlap of pixels between the balloon
    #   and the terrain.
    if overlap:
        # we have hit the wall!!!  oh noes!
        screen.blit(hitsurf, (0,0))

    # flip the display.
    pygame.display.flip() #updates the screen

    # # limit the frame rate to 40fps.
    # clock.tick(40)



pygame.quit()
