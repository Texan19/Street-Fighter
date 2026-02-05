"""
title: entity class
author: austin wp
date: 02/04/26
"""

import pygame

class Entity:
    def __init__(self, name=None, x=0, y=0, speed=10, hitPoints=0, damageOutput=0, jumpHeight=100):
        self._name = name
        self._x = x
        self._y = y
        self._position = (self._x, self._y)
        self._speed = speed
        self._hitPoints = hitPoints
        self._damageOutput = damageOutput
        self._jumpHeight = jumpHeight
        self._surface = pygame.Surface

    # accessor methods
    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getSpeed(self):
        return self._speed

    def getHitPoints(self):
        return self._hitPoints

    def getDamageOutput(self):
        return self._damageOutput

    def getJumpHeight(self):
        return self._jumpHeight

    def getSurface(self):
        return self._surface

    def getWidth(self):
        return self._surface.get_width()

    def getHeight(self):
        return self._surface.get_height()

    def getPosition(self):
        return self._position

    # modifier methods
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setPosition(self, x, y):
        self._x = x
        self._y = y
        self.updatePosition()

    def updatePosition(self):
        self._position = (self._x, self._y)
