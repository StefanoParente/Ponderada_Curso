import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.result = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        # Substitua os valores esperados com base nos dados reais
        self.assertEqual(self.result['race_count']['White'], 27816)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.result['average_age_men'], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.result['percentage_bachelors'], 16.4, places=1)

    def test_percentage_advanced_education_50k(self):
        self.assertAlmostEqual(self.result['percentage_advanced_education_50k'], 46.5, places=1)

    def test_percentage_non_advanced_education_50k(self):
        self.assertAlmostEqual(self.result['percentage_non_advanced_education_50k'], 17.4, places=1)

    def test_min_hours_per_week(self):
        self.assertEqual(self.result['min_hours_per_week'], 1)

    def test_percentage_min_hours_50k(self):
        self.assertAlmostEqual(self.result['percentage_min_hours_50k'], 10.0, places=1)

    def test_highest_percentage_country(self):
        self.assertEqual(self.result['highest_percentage_country'], 'Iran')
        self.assertAlmostEqual(self.result['highest_percentage'], 41.9, places=1)

    def test_most_popular_occupation_india(self):
        self.assertEqual(self.result['most_popular_occupation_india'], 'Prof-specialty')

if __name__ == "__main__":
    unittest.main()
