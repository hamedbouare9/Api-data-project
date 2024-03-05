import unittest
from companies_data import CompaniesData


class TestCompaniesData(unittest.TestCase):
    def setUp(self):
        self.new_instance = CompaniesData('0D43N0-E')
        self.excepted_companies = ["NILAND", "LOUDR FM", "SOUNDCLOUD"]
        self.excepted_interactions = 3

    def test_instance_industry_data(self):
        self.assertIsInstance(self.new_instance, CompaniesData)

    def test_method_values(self):
        self.assertListEqual(self.new_instance.get_targeted_companies_names(), self.excepted_companies)
        self.assertEqual(self.new_instance.count_number_interactions(), self.excepted_interactions)

