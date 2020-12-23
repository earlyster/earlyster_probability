"""
Test Binomial Distribution Class
"""
import unittest
import os
import sys
from earlyster_probability.binomial_distribution import Binomial

class TestBinomialClass(unittest.TestCase):
    '''Test Binomial Class'''
    def setUp(self):
        """Setup Binomial instance"""
        self.binomial = Binomial(0.4, 20)
        self.file = os.path.join(sys.path[0], 'numbers_binomial.txt')
        self.binomial.read_data_file(self.file)

    def test_initialization(self):
        """Initialization test"""
        self.assertEqual(self.binomial.probability_of_event, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.number_of_trials, 20, 'n value incorrect')

    def test_readdata(self):
        """Read data loaded from file test"""
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')

    def test_calculatemean(self):
        """Calculate mean"""
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)

    def test_calculatestdev(self):
        """Calculate Standard deviation"""
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)

    def test_replace_stats_with_data(self):
        """Replace stats with data"""
        probability_of_event, number_of_trials = self.binomial.replace_stats_with_data()
        self.assertEqual(round(probability_of_event,3), .615)
        self.assertEqual(number_of_trials, 13)

    def test_pdf(self):
        """Test Probability density function"""
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        """Test Addition of Binomial Using magic function"""
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two

        self.assertEqual(binomial_sum.probability_of_event, .4)
        self.assertEqual(binomial_sum.number_of_trials, 80)
