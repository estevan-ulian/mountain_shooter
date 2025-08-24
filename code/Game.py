#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import MENU_OPTION, WINDOW_WIDTH, WINDOW_HEIGHT
from code.Level import Level
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
            selected_menu = menu.run()

            if selected_menu in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', selected_menu, player_score)
                player_level = level.run(player_score)
                if player_level:
                    level = Level(self.window, 'Level2', selected_menu, player_score)
                    player_level = level.run(player_score)
            elif selected_menu == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
