#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter.font import Font
from random import choice
from pygame import Rect, Surface
import pygame
from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import COLOR_CYAN, COLOR_GREEN, ENEMY_SPAWN_TIME, EVENT_ENEMY, EVENT_TIMEOUT, MENU_OPTION, TIMEOUT_LEVEL, TIMEOUT_STEP, WINDOW_HEIGHT, COLOR_WHITE
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(loops=-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if entity.name == 'Player1':
                    self.level_text(
                        text_size=14, text=f'Player1 - Health: {entity.health} | Score: {entity.score}', text_color=COLOR_GREEN, text_pos=(10, 25))
                if entity.name == 'Player2':
                    self.level_text(
                        text_size=14, text=f'Player2 - Health: {entity.health} | Score: {entity.score}', text_color=COLOR_CYAN, text_pos=(10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    rand_enemy = choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(
                        EntityFactory.get_entity(rand_enemy))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == 'Player1':
                                player_score[0] = entity.score
                            if isinstance(entity, Player) and entity.name == 'Player2':
                                player_score[1] = entity.score
                        return True

                found_player = False
                for entity in self.entity_list:
                    if isinstance(entity, Player):
                        found_player = True

                if not found_player:
                    return False

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
