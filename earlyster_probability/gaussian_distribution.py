'''Gaussian Distribution module'''

import math
import warnings
import matplotlib.pyplot as plt
from .general_distribution import Distribution

class Gaussian(Distribution):

    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """

    def calculate_mean(self):
        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set
        """
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set

        """

        if sample:
            n_number = len(self.data) - 1
        else:
            n_number = len(self.data)
        mean = self.mean
        sigma = 0

        for data in self.data:
            sigma += (data-mean) ** 2

        sigma = math.sqrt(sigma / n_number)

        self.stdev = sigma

        return self.stdev


    def read_data_file(self, file_path, sample=True):
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data
        attribute.

        After reading in the file, the mean and standard deviation are
        calculated

        Args:
            file_path (string): path to the file to read for data,
                must have read access.
            sample (bool): whether the data represents a sample or population

        Returns:
            None

        """

        # This code opens a data file and appends the data to a list called data_list
        super().read_data_file(file_path)

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.hist(self.data)
        plt.title("Histogram of Data")
        plt.xlabel("Data")
        plt.ylabel("Count")
        plt.show()

    def pdf(self, point):
        """Probability density function calculator for the gaussian
        distribution.

        Args:
            point (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        return (1.0 \
        / (self.stdev * math.sqrt(2*math.pi))) * \
            math.exp(-0.5*((point - self.mean)/self.stdev)**2)

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        min_range = min(self.data)
        max_range = max(self.data)

         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x_number = []
        y_number = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x_number.append(tmp)
            y_number.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x_number, y_number)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x_number, y_number

    def __add__(self, other):
        """
        Funcaiton to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Guassian: Gaussian distribution
        """
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            sting: characteristics of the Gaussian
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

    def __getattr__(self, name):
        ''' will only get called for undefined attributes '''
        warnings.warn('No member "%s" contained in settings config.' % name)
        return ''
