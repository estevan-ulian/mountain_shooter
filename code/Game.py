#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            pygame.display.set_caption("Mountain Shooter")
            menu = Menu(self.window)
            menu.run()
            pass
        
