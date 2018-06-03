
from .Checker import Checker
from .Mower import Mower


class Worker:

    def __init__(self):
        self._checker = None
        self._area = None

    def treat_file(self, file_path):
        with open(file_path, "r", encoding='utf-8') as fp:
            lines = fp.read().splitlines()
        self._checker = Checker(lines)
        ret = self._checker.process()
        if ret == -1:
            return ret
        self._create_area(lines[0])
        ret = self._process(lines[1:])
        return ret

    def _create_area(self, area_line):
        area_indic = area_line.split()
        self._area = tuple([int(area_indic[0]), int(area_indic[1])])

    def _process(self, orders_list):
        mowers, positions = self._create_mowers(orders_list)
        if mowers is None:
            return -1
        self._move_mowers(orders_list, mowers, positions)

    def _create_mowers(self, orders_list):
        mowers = list()
        positions = dict()
        orders_count = len(orders_list)
        for n in range(0, orders_count, 2):
            orders = orders_list[n].split()
            x = int(orders[0])
            y = int(orders[1])
            orientation = orders[2]
            mower = Mower(x, y, orientation, max_x=self._area[0], max_y=self._area[1])
            mowers.append(mower)
            if x not in positions:
                positions[x] = set()
            if y in positions[x]:
                print('Error: Two mowers have a same position: {} {}'.format(x, y))
                return None, None
            positions[x].add(y)
        return mowers, positions

    def _move_mowers(self, orders_list,  mowers, positions):
        orders_count = len(orders_list)
        for m, n in enumerate(range(1, orders_count, 2)):
            mower = mowers[m]
            orders = list(orders_list[n])
            for order in orders:
                if order == 'A':
                    positions[mower.x].remove(mower.y)
                    mower.move(positions)
                    if mower.x not in positions:
                        positions[mower.x] = set()
                    positions[mower.x].add(mower.y)
                else:
                    mower.change_orientation(order)
            print(mower)
