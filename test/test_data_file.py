import unittest
import logging

from psr_formats import DataFile


class TestDataFile(unittest.TestCase):

    def setUp(self):
        self.data_file = DataFile("some/path")

    def test_loaded(self):
        self.assertTrue(not self.data_file.loaded)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
