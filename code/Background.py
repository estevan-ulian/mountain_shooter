#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, WINDOW_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
