#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WINDOW_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                bg_list = []
                for i in range(7):
                    bg_list.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    bg_list.append(Background(name=f'Level1Bg{i}', position=(WINDOW_WIDTH, 0)))
                return bg_list
