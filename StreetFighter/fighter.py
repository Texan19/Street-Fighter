"""
title: fighter class
author: austin wp
date: 02/04/26
"""

from entity import Entity
import pygame


class Fighter(Entity):
    def __init__(self, imageFileLocation):
        Entity.__init__(self)
        self.__imageFileLocation = imageFileLocation
        self._surface = pygame.image.load(self.__imageFileLocation).convert_alpha()

    def setScale(self, scaleX, scaleY=None):
        if scaleY == None:
            scaleY = scaleX

        self._surface = pygame.transform.scale(self._surface, (self.getWidth()*scaleX, self.getHeight()*scaleY))

    def move(self, inputs):
        if inputs[pygame.K_a]:
            self._x -= self._speed
        elif inputs[pygame.K_d]:
            self._x += self._speed

        self.updatePosition()

if __name__ == '__main__':
    from window import Window

    pygame.init()

    window = Window("street fighter testing")

    fighter = Fighter("imageSprites/fighterDummy.png")

    fighter.setScale(0.5)

    fighter.setPosition(0, window.getVirtualHeight() - fighter.getHeight())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        inputs = pygame.key.get_pressed()
        fighter.move(inputs)

        window.clearScreen()

        window.getScreen().blit(fighter.getSurface(), fighter.getPosition())

        window.updateFrame()