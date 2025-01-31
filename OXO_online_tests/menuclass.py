# menu class

import pygame
from time import *

# have functions for creating buttons and storing in list, displaying buttons
#  button sprites changing when hovering over

class menu(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.xlist = []
        self.ylist = []

    def createobj(self, image, dimensions, intx, inty):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, dimensions)
        self.objects.append(self.image)
        #initial coords
        self.xlist.append(intx)
        self.ylist.append(inty)

##    def displayobj(self):
##        for i in range(0, len(self.objects)):
##            self.screen.blit(self.objects[i], (self.xlist[i], self.ylist[i]))

    def displayobj(self, pos):
        self.screen.blit(self.objects[pos], (self.xlist[pos], self.ylist[pos]))

    def animateobj(self, imagelist, fps):
        for i in range(0, len(imagelist)):
            self.displayobj(imagelist[i])
            newtime = time()
            currentime = time()
            while newtime - currentime < fps:
                newtime = time()

            
    def changeobj(self, pos, image, dimensions, x, y):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, dimensions)
        self.objects[pos] = self.image
        #initial coords
        self.xlist[pos] = x
        self.ylist[pos] = y
