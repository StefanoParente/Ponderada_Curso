import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import matplotlib.pyplot as plt

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_line_plot(self):
        fig = draw_line_plot()
        self.assertIsInstance(fig, plt.Figure)

    def test_bar_plot(self):
        fig = draw_bar_plot()
        self.assertIsInstance(fig, plt.Figure)

    def test_box_plot(self):
        fig = draw_box_plot()
        self.assertIsInstance(fig, plt.Figure)

if __name__ == "__main__":
    unittest.main()
