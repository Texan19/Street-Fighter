"""
title: text class
author: austin wp
date: 02/04/26
"""

from colours import Colour
import pygame

class Text:
    """
    create a text object to be displayed on screen
    """
    def __init__(self, text, fontFamily="Arial"):
        self.__text = text
        self.__colour = Colour.white()
        self.__fontFamily = fontFamily
        self.__fontSize = 36
        self.__font = pygame.font.SysFont(self.__fontFamily, self.__fontSize)
        self.__surface = self.__font.render(self.__text, True, self.__colour)
        self.__x = 0
        self.__y = 0
        self.__position = (self.__x, self.__y)

    def getSurface(self):
        return self.__surface

    def getPosition(self):
        return self.__position

    def getTextWidth(self):
        return self.__surface.get_width()

    def getTextHeight(self):
        return self.__surface.get_height()

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)

    def setTextColour(self, colour):
        self.__colour = colour
        self.__surface = self.__font.render(self.__text, True, self.__colour)
        # we must update the surface after changing the colour to ensure the update goes through

    def setTextSize(self, newSize):
        self.__fontSize = newSize
        self.__font = pygame.font.SysFont(self.__fontFamily, self.__fontSize)
        self.__surface = self.__font.render(self.__text, True, self.__colour)

    def setTextFont(self, newFont):
        self.__fontFamily = newFont
        self.__font = pygame.font.SysFont(self.__fontFamily, self.__fontSize)
        self.__surface = self.__font.render(self.__text, True, self.__colour)

    def updateText(self, newText):
        self.__text = newText
        self.__surface = self.__font.render(self.__text, True, self.__colour)