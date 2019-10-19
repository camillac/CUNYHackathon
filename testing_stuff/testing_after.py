import os
import pygame
import math
from pygame.locals import *

pygame.display.init()
pygame.font.init()

logo = pygame.image.load("../turtle_left.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Turtles In Trash")

going = 1

screen_x = 1450
screen_y = 800
boundary_left = 725
boundary_up = -400
boundary_right = 2275
boundary_down = -1600
screen = pygame.display.set_mode((screen_x,screen_y)) #sets the display screen
# set display color as ocean blue
screen.fill((7,176,157))
pygame.display.flip()

### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision
def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join("..", i)).convert_alpha()

turtle = load_image("turtle_right.png")
trash = load_image("map.png")
ocean = load_image("ocean.jpg")


# create a mask for each of them.
turtle_mask = pygame.mask.from_surface(turtle, 50)
trash_mask = pygame.mask.from_surface(trash, 50)

turtle_rect = turtle.get_rect()
trash_rect = trash.get_rect()

# a message for if the balloon hits the terrain.
afont = pygame.font.Font(None, 16)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))
boundr = afont.render("Can't move anymore", 1, (255,255,255))


# start the main loop.

while going:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[QUIT] or keys[K_ESCAPE]:
        going = 0
    # if e.type == pygame.KEYDOWN:
    #     # move the balloon around, depending on the keys.
    if keys[K_LEFT]:
        print(trash_rect.x)
        if trash_rect.x +3 <= boundary_left:
            trash_rect.x += 3
        #turtle = load_image("turtle_left.png")
    if keys[K_RIGHT]:
        if trash_rect.x -3 >= boundary_right:
            trash_rect.x -= 3

        #turtle = load_image("turtle_right.png")

    if keys[K_UP]:
        if trash_rect.y +3 >= boundary_up:
            trash_rect.y += 3

    if keys[K_DOWN]:
        if trash_rect.y -3 <= boundary_down:
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
    screen.blit(pygame.transform.scale(ocean, (1450,800)), (0, 0)) #scales the image to the screen size
    screen.blit(trash, (trash_rect[0], trash_rect[1]) )
    screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center
    # draw the balloon rect, so you can see where the bounding rect would be.
    pygame.draw.rect(screen, (0,255,0), trash_rect, 1)


    # see if there was an overlap of pixels between the balloon
    #   and the terrain.
    if overlap:
        # we have hit the wall!!!  oh noes!
        screen.blit(hitsurf, (0,0))
        # screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center


        #screen.blit(turtle,(trash_rect.x-1, trash_rect.y-1)) #draws turtle in center
        #trash_rect.move(trash_rect.x-50, trash_rect.y-50)


    # flip the display.
    pygame.display.flip()

    # # limit the frame rate to 40fps.
    # clock.tick(40)



pygame.quit()
