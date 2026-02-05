"""
title: window class
author: Austin WP
date: 02/03/26
"""

import pygame

class Window:
    """
    create a window that will be displayed on the screen
    """

    def __init__(self, title, width=1400, height=800, fps=30):
        self.__title = title # text that appears in the title bar of the window
        self.__width = width # width of window
        self.__height = height # height of window
        self.__dimensions = (self.__width, self.__height) # window dimensions
        self.__fps = fps # frames per second
        self.__bgColour = (50, 50, 50) # RGB values - this makes dark grey
        self.__clock = pygame.time.Clock() # clock object that tracks time
        self.__screen = pygame.display.set_mode(self.__dimensions) # base surface that all surfaces are overlaid onto
        self.__screen.fill(self.__bgColour) # colours the screen surface
        pygame.display.set_caption(self.__title) # sets the window caption with the title

    # accessor methods
    def getScreen(self):
        return self.__screen

    def getVirtualWidth(self):
        return self.__width

    def getVirtualHeight(self):
        return self.__height

    # modifier methods
    def updateFrame(self):
        self.__clock.tick(self.__fps) # waits the appropriate amount of time (in milliseconds) based on FPS before finishing the loop
        pygame.display.flip() # updates the computer screen with the new frame

    def clearScreen(self):
        self.__screen.fill(self.__bgColour)

if __name__ == '__main__':
    window = Window("Window Test")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.updateFrame()