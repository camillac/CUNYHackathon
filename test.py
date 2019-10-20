import os
import pygame
import math
from math import sin
from pygame.locals import *
import time
import pdb

main_dir = os.path.split(os.path.abspath(__file__))[0]

pygame.display.init()
pygame.font.init()

logo = pygame.image.load("turt_right.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Turtles In Trash")
#self._running = True
healthbar_rect = pygame.Rect(0,0,200,30) #green
healthbar_surf= pygame.Surface((healthbar_rect[2], healthbar_rect[3]))
healthbar_surf.fill((0,255,0))

def bad_ending():
    going = 1
    count = 0
    screen_x = 1450
    screen_y = 800
    going = 1

    screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
    #screen.fill((255,255,255))
    ocean = load_image("bad.png")
    screen.blit(pygame.transform.scale(ocean, (1450,800)), (0, 0)) #scales the image to the screen size

    pygame.display.flip()
    button = pygame.Rect(screen_x/2-200, screen_y/2, 200, 100)
    while going:
        for event in pygame.event.get():
            print("h")
            if event.type == pygame.QUIT:
                return False
                print("no")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                print("idjod")
                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    #ye = True
                    print('button was pressed at {0}'.format(mouse_pos))
                    # ye = True
                    on_cleanup()

            pygame.draw.rect(screen, [52, 88, 235], button)  # draw button
            print("ifjoei")

            pygame.display.update()
            print("hue")

def good_ending():
    going = 1
    count = 0
    screen_x = 1450
    screen_y = 800
    going = 1

    screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
    #screen.fill((255,255,255))
    ocean = load_image("good.png")
    screen.blit(pygame.transform.scale(ocean, (1450,800)), (0, 0)) #scales the image to the screen size

    pygame.display.flip()
    button = pygame.Rect(screen_x/2-200, screen_y/2, 200, 100)
    while going:
        for event in pygame.event.get():
            print("h")
            if event.type == pygame.QUIT:
                return False
                print("no")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                print("idjod")
                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    #ye = True
                    print('button was pressed at {0}'.format(mouse_pos))
                    # ye = True
                    on_cleanup()

            pygame.draw.rect(screen, [52, 88, 235], button)  # draw button
            print("ifjoei")

            pygame.display.update()
            print("hue")

def damage(counter):

    if counter <=100:
        damage_rect = pygame.Rect(0,0,(counter*2),30)
        pygame.draw.rect(healthbar_surf, (255,0,0), damage_rect, 0)
    else:
        bad_ending()
        print ("Too many hits! game over")
        #pygame.quit()

def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(os.path.join(".", i)).convert_alpha()

def on_cleanup():
    pygame.quit()

def on_execute():
    counter = 0
    going = 1

    speed = 15

    screen_x = 1450
    screen_y = 800
    boundary_left = 725
    boundary_up = -400
    boundary_right = -3050
    boundary_down = -2200


    screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
    # set display color as ocean blue
    screen.fill((7,176,157))
    pygame.display.flip()

    ### MASK CODE TAKEN FROM SAMPLE PROGRAM - https://github.com/illume/pixel_perfect_collision

    turtle = load_image("turt_right.png")
    map = load_image("map.png")
    baby = load_image("baby.png")
    # map = pygame.transform.scale2x(map)
    ocean = load_image("ocean.png")
    garbage = load_image("garbage.png")#NEW

    # create a mask for each of them.
    turtle_mask = pygame.mask.from_surface(turtle, 50)
    map_mask = pygame.mask.from_surface(map, 50)
    baby_mask = pygame.mask.from_surface(baby, 50)
    garbage_mask = pygame.mask.from_surface(garbage, 50)#NEW

    turtle_rect = turtle.get_rect()
    map_rect = map.get_rect()
    baby_rect = baby.get_rect()
    garbage_rect = garbage.get_rect() #NEW

    # a message for if the map hits the terrain.
    afont = pygame.font.Font(None, 16)
    hitsurf = afont.render("Hit!!!  Oh noes!!", 1, (255,255,255))
    boundr = afont.render("Can't move anymore", 1, (255,255,255))


    if screen.get_bitsize() == 8:
        screen.set_palette(ocean.get_palette())
    else:
        ocean = ocean.convert_alpha()

    anim = 0.0

    # mainloop
    xblocks = range(0, screen_x, 20)
    yblocks = range(0, screen_y, 20)

    # start the main loop.

    map_rect[0] = -180
    map_rect[1] = -120

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
                turtle = load_image("turt_left.png")
                # turtle_mask = pygame.mask.from_surface(turtle, 50)
        if keys[K_RIGHT]:
            # print(map_rect.x)
            if map_rect.x - speed >= boundary_right:
                map_rect.x -= speed
                turtle = load_image("turt_right.png")
                # turtle_mask = pygame.mask.from_surface(turtle, 50)
        if keys[K_UP]:
            # print(map_rect.y)
            if map_rect.y + speed <= 0:
                map_rect.y += speed
                turtle = load_image("turt_up.png")
                # turtle_mask = pygame.mask.from_surface(turtle, 50)
        if keys[K_DOWN]:
            # print(map_rect.y)
            if map_rect.y - speed >= boundary_down:
                map_rect.y -= speed
                turtle = load_image("turt_down.png")
                # turtle_mask = pygame.mask.from_surface(turtle, 50)


        # see how far the map rect is offset from the turtle rect.
        bx, by = (map_rect[0], map_rect[1]) #NEW
        offset_x = bx - math.floor(screen_x/2-150)#turtle_rect[0]
        offset_y = by - math.floor(screen_y/2-100)#turtle_rect[1]


        #print bx, by
        hitwall = turtle_mask.overlap(map_mask, (offset_x, offset_y)) #NEW
        overlap = turtle_mask.overlap(garbage_mask, (offset_x, offset_y)) #NEW
        touchbaby = turtle_mask.overlap(baby_mask, (offset_x, offset_y))

        #
        last_bx, last_by = bx, by


        # draw the background color, and the terrain.
        screen.fill((7,176,157))

        anim = anim + 0.04
        for x in xblocks:
            xpos = (x + (sin(anim + x * 0.01) * 15)) + 20
            for y in yblocks:
                ypos = (y + (sin(anim + y * 0.01) * 15)) + 20
                screen.blit(ocean, (x, y), (xpos, ypos, 20, 20))

        # see if there was an overlap of pixels between the map
        #   and the terrain.
        if touchbaby:
            if keys[K_LEFT]:
                map_rect.x -= speed
            if keys[K_RIGHT]:
                map_rect.x += speed
            if keys[K_UP]:
                map_rect.y -= speed
            if keys[K_DOWN]:
                map_rect.y += speed
            print("BABYYYYY")
            good_ending()
            #turtle image becomes turtle + baby image?
            #stop baby from moving w the map?
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
            counter +=1
            damage(counter)
            print(counter)
            print("COLLISION!")
        if hitwall: #NEW
            if keys[K_LEFT]:
                map_rect.x -= speed
            if keys[K_RIGHT]:
                map_rect.x += speed
            if keys[K_UP]:
                map_rect.y -= speed
            if keys[K_DOWN]:
                map_rect.y += speed


        # draw map + turtle
        red=(255,0,0)
        green=(0,255,0)


        #counter = 0
        screen.blit(map, (map_rect[0], map_rect[1]) )
        screen.blit(turtle,(screen_x/2-150,screen_y/2-100)) #draws turtle in center
        screen.blit(baby, (map_rect[0], map_rect[1]) )
        screen.blit(garbage, (map_rect[0], map_rect[1]) ) #NEW
        screen.blit(healthbar_surf, (10, 10)) #location on screen
        # draw the map rect, so you can see where the bounding rect would be.
        pygame.draw.rect(screen, (0,255,0), map_rect, 1)


        # flip the display.
        pygame.display.flip()
        time.sleep(0.01)

        # # limit the frame rate to 40fps.
    # clock.tick(40)
    on_cleanup()


def story():
    going = 1
    count = 0
    screen_x = 1450
    screen_y = 800
    going = 1
    afont = pygame.font.Font(None, 150)

    welcome = afont.render("Help Josie get to her baby!", 1, (138, 203, 230))

    wel2 = afont.render("Avoid the trash so she can", 1, (138, 203, 230))

    wel3 = afont.render("get to her baby!", 1, (138, 203, 230))
    afont = pygame.font.Font(None, 100)

    cl_but = afont.render("Click the button to continue", 1, (138, 203, 230))


    screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
    #screen.fill((255,255,255))
    ocean = load_image("ocean.png")
    screen.blit(pygame.transform.scale(ocean, (1450,800)), (0, 0)) #scales the image to the screen size

    pygame.display.flip()
    button = pygame.Rect(screen_x/2-200, screen_y/2, 200, 100)
    while going:
        screen.blit(welcome, (20,screen_y/9))
        screen.blit(wel2, (20 ,screen_y/7 + 100))
        screen.blit(wel3, (200,screen_y/7 + 200))

        screen.blit(cl_but, (90 ,screen_y-70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    #ye = True
                    print('button was pressed at {0}'.format(mouse_pos))
                    # ye = True
                    on_execute()

            pygame.draw.rect(screen, [52, 88, 235], button)  # draw button

            pygame.display.update()

def starter_page():
    pygame.init()

    # print("f")
    screen_x = 1450
    screen_y = 800
    going = 1
    myfont = pygame.font.SysFont("KAUSHAN SCRIPT",150)

    welcome = myfont.render("Welcome to Turtles In Trash!", 1, (255,255,255))
    myfont = pygame.font.SysFont("KAUSHAN SCRIPT",100)

    cl_but = myfont.render("Click the button to play", 1, (255,255,255))



    screen = pygame.display.set_mode((screen_x,screen_y), HWSURFACE | DOUBLEBUF) #sets the display screen
    ocean = load_image("ocean.png")
    redSquare = pygame.image.load("turt_right.png").convert_alpha()
    pygame.transform.scale2x(redSquare)
    redSquare_rect = redSquare.get_rect()
    redSquare_rect.x = screen_x/2
    redSquare_rect.y = screen_y/2 +20
    second_t = pygame.image.load("turt_light.png").convert_alpha()
    pygame.transform.scale2x(second_t)


    screen.blit(pygame.transform.scale(ocean, (1450,800)), (0, 0)) #scales the image to the screen size    pygame.display.flip()
    button = pygame.Rect(screen_x/2-50, screen_y/2+60, 200, 200)
    # screen.blit(welcome, (0,screen_y/4))
    # screen.blit(cl_but, (screen_x/3-100 ,screen_y/3 + 40))
    welc = load_image("welcome")
    screen.blit(welc, (0, 0)) #scales the image to the screen size    pygame.display.flip()

    screen.blit(redSquare ,(screen_x/2-50, screen_y/2+60)) # paint to screen
    print(screen_x/2)
    print(screen_y+100)
    pygame.display.flip() # paint screen one time


    while going:
        for event in pygame.event.get():
            # print("h")
            if event.type == pygame.QUIT:
                return False
                # print("no")
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("he")
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                # print("idjod")
                print(mouse_pos)
                print(redSquare_rect.x)
                print(redSquare_rect.y)
                print(redSquare_rect)


                x, y = event.pos

                if button.collidepoint(mouse_pos):
                    print('clicked on image')
                # if button.get_rect().collidepoint(mouse_pos):
                #     # prints current location of mouse
                #     #ye = True
                #     print('button was pressed at {0}'.format(mouse_pos))
                    # ye = True
                    #story()
                    screen.blit(second_t ,(screen_x/2-50, screen_y/2+60)) # paint to screen
                    pygame.display.flip() # paint screen one time


                    on_execute()

            # pygame.draw.rect(screen, [255, 0, 0], redSquare)  # draw button

            # print("ifjoei")

            pygame.display.update()
def main():
    starter_page()


main()
