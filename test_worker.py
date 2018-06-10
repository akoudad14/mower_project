
from Objects.Worker import Worker
import unittest
import sys
import io


class WorkerTest(unittest.TestCase):

    """
    Test case use for test Worker methods
    """

    def setUp(self):
        self.worker = Worker()

    def test_project_input(self):
        lines = '5 5\n1 2 N\nGAGAGAGAA\n3 3 E\nAADAADADDA'.split('\n')
        output = self._launch_work(lines)
        self.assertEqual(output, '1 3 N\n5 1 E\n')

    def test_multi_mowers(self):
        lines = '5 5\n1 2 N\nGAGAGAGAA\n3 3 E\nAADAADADDA\n4 5 S\nDAAAGA\n1 1 W\nADAGADA'.split('\n')
        output = self._launch_work(lines)
        self.assertEqual('1 3 N\n5 1 E\n1 4 S\n0 3 N\n', output)

    def test_many_movements(self):
        lines = '5 5\n1 2 N\nGAGAGAAADAAAGAAGAAAAAGAADAAAA\n3 3 E\nAAAADDAAAADDAAGADAAAAADDAAA'.split('\n')
        output = self._launch_work(lines)
        self.assertEqual('0 5 N\n1 4 W\n', output)

    def _launch_work(self, lines):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        ret = self.worker.work(lines)
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        self.assertEqual(ret, 0)
        return output
