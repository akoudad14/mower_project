
class Checker:

    def __init__(self, lines):
        self._lines = lines

    def process(self):
        ret = self._check_area(self._lines[0])
        if ret == -1:
            return ret
        return self._check_mowers(self._lines[1:])

    def _check_area(self, area_coords):
        coords = area_coords.split()
        if len(coords) != 2:
            print('Error: Bad indications for area size: {}'.format(area_coords))
            return -1
        return self._check_coordinates(coords, 'area')

    def _check_mowers(self, mowers):
        for n, mower in enumerate(mowers, 1):
            if n % 2 == 1:
                coords = mower.split()
                if len(coords) != 3:
                    print('Error: Bad indications for mower location: {}'.format(mower))
                    return -1
                ret = self._check_coordinates(coords[:2], 'mower')
                if ret == -1:
                    return ret
                if coords[2] not in ('N', 'E', 'W', 'S'):
                    print('Error: Bad cardinal point: {}'.format(coords[2]))
                    return -1
            else:
                movements = mower.split()
                if len(movements) != 1:
                    print('Error: Bad movements: {}'.format(mower))
                    return -1
                movements = set(mower)
                for movement in movements:
                    if movement not in ('D', 'G', 'A', 'D'):
                        print('Error: Bad movement: {}'.format(movement))
                        return -1
        return 0

    def _check_coordinates(self, coords, type_):
        for coord in coords:
            try:
                coord = int(coord)
            except ValueError:
                print('Error: Bad type for {} coordinates: {}'.format(type_, coord))
                return -1
            else:
                if coord <= 0:
                    print('Error: Bad value for {} coordinates: {}'.format(type, coord))
                    return -1
        return 0
