import unittest

import h2o

class TestH2o(unittest.TestCase):
    def test_init_read(self):
        h2o.init()
        train = h2o.import_file("/input/tests/data/train.csv", destination_frame="train")
        self.assertEqual(19, train.nrow)
