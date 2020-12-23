"""Binomial Distribution Module
Contains Binomial Class
"""
from earlyster_probability.gaussian_distribution import Gaussian
import math
import matplotlib.pyplot as plt
from .general_distribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the
        data file
        p (float) representing the probability of an event occurring
        n (int) number of trials
    """
    def __init__(self, prob=.5, size=20):
        self.number_of_trials = size
        self.probability_of_event = prob
        Distribution.__init__(self, self.calculate_mean(),
            self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.probability_of_event * self.number_of_trials
        return self.mean



    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set
        """

        self.stdev = math.sqrt(self.number_of_trials * \
            self.probability_of_event * (1 - self.probability_of_event))

        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        self.number_of_trials = len(self.data)
        self.probability_of_event = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.probability_of_event, self.number_of_trials

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x = ['0', '1'], height = [(1 - self.probability_of_event) \
            * self.number_of_trials, self.probability_of_event \
                * self.number_of_trials])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        a_number = math.factorial(self.number_of_trials) / (math.factorial(k) \
            * (math.factorial(self.number_of_trials - k)))
        b_number = (self.probability_of_event ** k) \
            * (1 - self.probability_of_event) ** (self.number_of_trials - k)
        return a_number * b_number

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x_number values for the pdf plot
            list: y_number values for the pdf plot

        """

        x_number = []
        y_number = []

        # calculate the x values to visualize
        for i in range(self.number_of_trials + 1):
            x_number.append(i)
            y_number.append(self.pdf(i))

        # make the plots
        plt.bar(x_number, y_number)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x_number, y_number

    def __add__(self, other: Gaussian):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.probability_of_event == other.probability_of_event, 'p values are not equal'
        except AssertionError as error:
            print("Assertion Error. {}".format(error))
            raise

        result = Binomial()
        result.number_of_trials = self.number_of_trials + other.number_of_trials
        result.probability_of_event = self.probability_of_event
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.probability_of_event, \
            self.number_of_trials)
