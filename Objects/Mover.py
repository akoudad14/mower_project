
from enum import Enum


class Mover:

    def __init__(self, max_x, max_y):
        self._mower = None
        self._max_x = int(max_x)
        self._max_y = int(max_y)

    def create_mower(self, x, y, orientation):
        self._mower = Enum('Mower', {'X': int(x), 'Y': int(y), 'ORIENT': orientation})

    def change_orientation(self, movement):
        if movement == 'D':
            if self._mower.ORIENT.value == 'N':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'E'})
            elif self._mower.ORIENT.value == 'E':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'S'})
            elif self._mower.ORIENT.value == 'S':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'W'})
            else:
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'N'})
        else:
            if self._mower.ORIENT.value == 'N':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'W'})
            elif self._mower.ORIENT.value == 'E':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'N'})
            elif self._mower.ORIENT.value == 'S':
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'E'})
            else:
                self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value, 'ORIENT': 'S'})

    def move(self):
        if self._mower.ORIENT.value == 'N' and self._mower.Y.value < self._max_x:
            self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value + 1,
                                         'ORIENT': self._mower.ORIENT.value})
        elif self._mower.ORIENT.value == 'E' and self._mower.X.value < self._max_y:
            self._mower = Enum('Mower', {'X': self._mower.X.value + 1, 'Y': self._mower.Y.value,
                                         'ORIENT': self._mower.ORIENT.value})
        elif self._mower.ORIENT.value == 'S' and self._mower.Y.value > 0:
            self._mower = Enum('Mower', {'X': self._mower.X.value, 'Y': self._mower.Y.value - 1,
                                         'ORIENT': self._mower.ORIENT.value})
        elif self._mower.X.value > 0:
            self._mower = Enum('Mower', {'X': self._mower.X.value - 1, 'Y': self._mower.Y.value,
                                         'ORIENT': self._mower.ORIENT.value})

    def print_mower_position(self):
        print(' '.join([str(self._mower.X.value), str(self._mower.Y.value), self._mower.ORIENT.value]))
