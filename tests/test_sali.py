import sys
sys.path.insert(0, "../src")
import unittest
from sali import Sali

class TestSali(unittest.TestCase):

    def setUp(self):
        self.app = Sali()

    def test_calc_inss(self):
        self.assertAlmostEqual(self.app.inss_calc(1100), 82.5)
        # self.assertAlmostEqual(self.app.inss_calc(2100), 1927.50, 2)
        self.assertAlmostEqual(self.app.inss_calc(3250), 307.40)
        # self.assertAlmostEqual(self.app.inss_calc(5120), 4551.90, 2)
        self.assertAlmostEqual(self.app.inss_calc(21000), 751.97)

    def test_calc_irrf(self):
        self.assertAlmostEqual(self.app.irrf_calc(1017.50), 0)
        # self.assertAlmostEqual(self.app.irrf_calc(1927.50), 1925.74, 2)
        self.assertAlmostEqual(self.app.irrf_calc(2942.60), 86.59)
        # self.assertAlmostEqual(self.app.irrf_calc(4551.90), 4163.85, 2)
        self.assertAlmostEqual(self.app.irrf_calc(20248.03), 4698.85)

if __name__ == '__main__':
    unittest.main()
