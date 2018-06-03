

class Mower:

    def __init__(self, x, y, orientation, max_x, max_y):
        self.x = x
        self.y = y
        self._max_x = max_x
        self._max_y = max_y
        self._orientations = ['N', 'E', 'S', 'W']
        self._orientation = self._orientations.index(orientation)
        self._moves = {'N': 1, 'E': 1, 'W': -1, 'S': -1}

    def change_orientation(self, movement):
        if movement == 'G':
            self._orientation -= 1
        else:
            self._orientation += 1
        if self._orientation < 0:
            self._orientation = 3
        if self._orientation > 3:
            self._orientation = 0

    def move(self, other_positions):
        cardinal_point = self._orientations[self._orientation]
        if cardinal_point in ('N', 'S'):
            self._vertical_move(self._moves[cardinal_point], other_positions)
        else:
            self._horizontal_move(self._moves[cardinal_point], other_positions)

    def _horizontal_move(self, value, other_positions):
        self.x += value
        if self.x < 0:
            self.x = 0
        if self.x > self._max_x:
            self.x = self._max_x
        if self.x in other_positions and self.y in other_positions[self.x]:
            self.x -= value

    def _vertical_move(self, value, other_positions):
        self.y += value
        if self.y < 0:
            self.y = 0
        if self.y > self._max_y:
            self.y = self._max_y
        if self.x in other_positions and self.y in other_positions[self.x]:
            self.y -= value

    def __str__(self):
        cardinal_point = self._orientations[self._orientation]
        return ' '.join([str(self.x), str(self.y), cardinal_point])