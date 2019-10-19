import os
import pygame
from pygame.locals import *

pygame.display.init()
pygame.font.init()

pygame.display.set_caption("Turtles In Trash")

going = 1

screen = pygame.display.set_mode((500,500))

# set display color as ocean blue
screen.fill((7,176,157))
pygame.display.flip()

### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision
def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join(".", i)).convert_alpha()

trash = load_image("turtle.png")
turtle = load_image("terrain1.png")

# create a mask for each of them.
trash_mask = pygame.mask.from_surface(trash, 50)
turtle_mask = pygame.mask.from_surface(turtle, 50)

trash_rect = trash.get_rect()
turtle_rect = turtle.get_rect()

# a message for if the balloon hits the terrain.
afont = pygame.font.Font(None, 16)
hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))


# start the main loop.

while going:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[QUIT] or keys[K_ESCAPE]:
        going = 0
    # if e.type == pygame.KEYDOWN:
    #     # move the balloon around, depending on the keys.
    if keys[K_LEFT]:
        turtle_rect.x -= 1
        # turtle = load_image("turtle2.png")
    if keys[K_RIGHT]:
        turtle_rect.x += 1

    if keys[K_UP]:
        turtle_rect.y -= 1
    if keys[K_DOWN]:
        turtle_rect.y += 1

    # see how far the balloon rect is offset from the terrain rect.
    bx, by = (turtle_rect[0], turtle_rect[1])
    offset_x = bx - trash_rect[0]
    offset_y = by - trash_rect[1]

    #print bx, by
    overlap = trash_mask.overlap(turtle_mask, (offset_x, offset_y))

    #
    last_bx, last_by = bx, by


    # draw the background color, and the terrain.
    screen.fill((7,176,157))
    screen.blit(trash, (0,0))

    # draw the balloon.
    screen.blit(turtle, (turtle_rect[0], turtle_rect[1]) )

    # draw the balloon rect, so you can see where the bounding rect would be.
    pygame.draw.rect(screen, (0,255,0), turtle_rect, 1)


    # see if there was an overlap of pixels between the balloon
    #   and the terrain.
    if overlap:
        # we have hit the wall!!!  oh noes!
        screen.blit(hitsurf, (0,0))

    # flip the display.
    pygame.display.flip()

    # # limit the frame rate to 40fps.
    # clock.tick(40)



pygame.quit()
