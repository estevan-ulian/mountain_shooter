#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font
from pygame import Rect, Surface
import pygame.image

from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, WINDOW_WIDTH, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(loops=-1)
        while True:
            # DRAW IMAGES AND TEXTS
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE,
                           text_center_pos=((WINDOW_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE,
                           text_center_pos=((WINDOW_WIDTH / 2), 120))

            # DRAW MENU OPTIONS
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=22, text=MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=(
                        (WINDOW_WIDTH / 2), 180 + (i * 30)))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=(
                        (WINDOW_WIDTH / 2), 180 + (i * 30)))

            # CHECK ALL EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
