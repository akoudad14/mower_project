
from .Checker import Checker
from .Mover import Mover


class Worker:

    def __init__(self):
        self._checker = None
        self._mover = None

    def work(self, lines):
        self._checker = Checker(lines)
        ret = self._checker.process()
        if ret == -1:
            return ret
        self._create_mover(lines[0])
        self._process(lines[1:])
        return ret

    def _create_mover(self, area_line):
        area_indic = area_line.split()
        self._mover = Mover(area_indic[0], area_indic[1])

    def _process(self, orders_list):
        for n, orders in enumerate(orders_list):
            if n % 2 == 0:
                mower_coordinate = orders.split()
                self._mover.create_mower(mower_coordinate[0], mower_coordinate[1], mower_coordinate[2])
            else:
                orders = list(orders)
                for order in orders:
                    if order == 'A':
                        self._mover.move()
                    else:
                        self._mover.change_orientation(order)
                self._mover.print_mower_position()
