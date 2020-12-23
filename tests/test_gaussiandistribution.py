"""
Test Gaussian Distribution Class
"""
import unittest
import os
import sys
from earlyster_probability.gaussian_distribution import Gaussian

class TestGaussianDistribution(unittest.TestCase):
    """
    Unit tests
    """
    def setUp(self):
        """Setup Gaussian instance"""
        self.gaussian = Gaussian(25, 2)
        self.file = os.path.join(sys.path[0], 'numbers.txt')

    def test_initialization(self):
        """Test Initialization"""
        self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
        self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_pdf(self):
        """Test Probablility Density Function (PDF)"""
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.19947,\
         'pdf function does not give expected result')

    def test_meancalculation(self):
        """Test Mean Calculation"""
        self.gaussian.read_data_file(self.file, True)
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)),
            'calculated mean not as expected')

    def test_stdevcalculation(self):
        """Test standard deviation calculation"""
        self.gaussian.read_data_file(self.file, True)
        self.assertEqual(round(self.gaussian.stdev, 2), 92.87,
            'sample standard deviation incorrect')
        self.gaussian.read_data_file(self.file, False)
        self.assertEqual(round(self.gaussian.stdev, 2), 88.55,
            'population standard deviation incorrect')

    def test_add(self):
        """Test custom adding"""
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)

    def test_repr(self):
        """Test print string"""
        gaussian_one = Gaussian(25, 3)
        self.assertEqual(str(gaussian_one), "mean 25, standard deviation 3")
