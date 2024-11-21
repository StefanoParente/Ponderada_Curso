import unittest
import pandas as pd
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTests(unittest.TestCase):
    def setUp(self):
        self.df = df = pd.read_csv('/Users/stefanoparente/Desktop/Ponderada_Curso/Medical_data_visualizer/medical.examination.csv')

    def test_overweight_column(self):
        self.df['BMI'] = self.df['weight'] / ((self.df['height'] / 100) ** 2)
        self.df['expected_overweight'] = (self.df['BMI'] > 25).astype(int)
        self.assertTrue('overweight' in self.df.columns, "Column 'overweight' is missing.")
        pd.testing.assert_series_equal(self.df['overweight'], self.df['expected_overweight'], check_dtype=False)

    def test_cat_plot(self):
        # Generate the cat plot and verify it has the correct type
        fig = draw_cat_plot()
        self.assertEqual(fig.__class__.__name__, 'Figure', "The returned object is not a matplotlib Figure.")

    def test_heat_map(self):
        # Generate the heat map and verify it has the correct type
        fig = draw_heat_map()
        self.assertEqual(fig.__class__.__name__, 'Figure', "The returned object is not a matplotlib Figure.")

if __name__ == '__main__':
    unittest.main()

