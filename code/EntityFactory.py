#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                bg_list = []
                for i in range(7):
                    bg_list.append(Background(
                        name=f'Level1Bg{i}', position=(0, 0)))
                    bg_list.append(Background(
                        name=f'Level1Bg{i}', position=(WINDOW_WIDTH, 0)))
                return bg_list
            case 'Player1':
                return Player(name='Player1', position=(10, WINDOW_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Player2', position=(10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', position=(WINDOW_WIDTH + 10, randint(40, WINDOW_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', position=(WINDOW_WIDTH + 10, randint(40, WINDOW_HEIGHT - 40)))
