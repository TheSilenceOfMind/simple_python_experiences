import unittest as ut
from unittest.test import __main__

import testing_11.city_functions as cf


class CitiesTestCase(ut.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """If func work appropriatly?"""
        result = cf.get_info('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population(self):
        """city country population"""
        res = cf.get_info('santiago', 'Chile', 130)
        self.assertEqual('Santiago, Chile, 130', res)

if __main__ == '__main__':
    ut.main()