#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter.font import Font
from random import choice
from pygame import Rect, Surface
import pygame
from code.EntityMediator import EntityMediator
from code.Const import ENEMY_SPAWN_TIME, EVENT_ENEMY, MENU_OPTION, WINDOW_HEIGHT, COLOR_WHITE
from code.EntityFactory import EntityFactory
from code.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = 20000  # 20 seconds
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(loops=-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    rand_enemy = choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(EntityFactory.get_entity(rand_enemy))

            # printed text
            self.level_text(
                text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(
                text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_WHITE, text_pos=(10, WINDOW_HEIGHT - 35))
            self.level_text(
                text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WINDOW_HEIGHT - 20))

            pygame.display.flip()
            
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
