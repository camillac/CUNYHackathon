
# import the pygame module, so you can use it
from pygame.locals import *
import pygame



class Player:
        x = 10
        y = 10
        speed = 1

        def moveRight(self):
            self.x = self.x + self.speed

        def moveLeft(self):
            self.x = self.x - self.speed

        def moveUp(self):
            self.y = self.y - self.speed

        def moveDown(self):
            self.y = self.y + self.speed

class Trash:
        x = 100
        y = 10

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False


class App:

        windowWidth = 800
        windowHeight = 600
        player = 0

        def __init__(self):
            self._running = True
            self._display_surf = None
            self._image_surf = None
            self._image_surf1 = None
            self.player = Player()
            self.trash= Trash()
            self.game = Game()

        def on_init(self):
            pygame.init()
            self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

            pygame.display.set_caption('Pygame pythonspot.com example')
            self._running = True
            self._image_surf = pygame.image.load("turtle.png").convert()
            self._image_surf1 = pygame.image.load("trash.png").convert()

        def on_event(self, event):
            if event.type == QUIT:
                self._running = False

        def on_loop(self): #COLLISION STUFF UNNECESSARY
            # does snake eat apple?
            #for i in range(0,self.player.length):
                if self.game.isCollision(self.trash.x,self.trash.y,self.player.x, self.player.y,44):
                    print ("You lose! collision!")
                pass

        def on_render(self):
            self._display_surf.fill((0,0,0))
            self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
            pygame.display.flip()

        def on_cleanup(self):
            pygame.quit()

        def on_execute(self):
            if self.on_init() == False:
                self._running = False

            while( self._running ):
                pygame.event.pump()
                keys = pygame.key.get_pressed()

                if (keys[K_RIGHT]):
                    self.player.moveRight()

                if (keys[K_LEFT]):
                    self.player.moveLeft()

                if (keys[K_UP]):
                    self.player.moveUp()

                if (keys[K_DOWN]):
                    self.player.moveDown()

                if (keys[K_ESCAPE]):
                    self._running = False

                self.on_loop()
                self.on_render()
            self.on_cleanup()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    theApp = App()
    theApp.on_execute()
