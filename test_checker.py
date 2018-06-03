
from Objects.Checker import Checker
import unittest
import sys
import io


class CheckerTest(unittest.TestCase):

    """
    Test case use for test Checker methods
    """

    def test_project_input(self):
        self.checker = Checker('5 5\n1 2 N\nGAGAGAGAA\n3 3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process(equal=0)
        self.assertEqual('', output)

    def test_area_size(self):
        self.checker = Checker('5 5 5\n1 2 N\nGAGAGAGAA\n3 3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad indications for area size', output)

    def test_coordinate_type(self):
        self.checker = Checker('5 5\n1 S N\nGAGAGAGAA\n3 3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad type for ', output)

    def test_coordinate_value(self):
        self.checker = Checker('5 5\n1 2 N\nGAGAGAGAA\n3 -3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad value for ', output)

    def test_mower_location(self):
        self.checker = Checker('5 5\n1 2 3 N\nGAGAGAGAA\n3 3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad indications for mower location', output)

    def test_cardinal_points(self):
        self.checker = Checker('5 5\n1 2 N\nGAGAGAGAA\n3 3 F\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad cardinal point:', output)

    def test_mower_movements(self):
        self.checker = Checker('5 5\n1 2 N\nGA GAGAGAA\n3 3 E\nAADAADADDA'.split('\n'))
        output = self._launch_process()
        self.assertIn('Error: Bad movement:', output)

    def _launch_process(self, equal=-1):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        ret = self.checker.process()
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        self.assertEqual(ret, equal)
        return output