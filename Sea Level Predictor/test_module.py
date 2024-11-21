import unittest
from sea_level_predictor import draw_plot

class SeaLevelTestCase(unittest.TestCase):
    def test_draw_plot(self):
        try:
            ax = draw_plot()
            self.assertIsNotNone(ax)
        except Exception as e:
            self.fail(f"O teste falhou devido a um erro: {e}")

if __name__ == "__main__":
    unittest.main()
