#!/usr/bin/env python3

"""  Normal class """


class Normal:
    """
    class that represents normal distribution

    class constructor:
        def __init__(self, data=None, mean=0., stddev=1.)

    instance attributes:
        mean [float]: the mean of the distribution
        stddev [float]: the standard deviation of the distribution

    instance methods:
        def z_score(self, x): calculates the z-score of a given x-value
        def x_value(self, z): calculates the x-value of a given z-score
        def pdf(self, x): calculates PDF for given x-value
        def cdf(self, x): calculates CDF for given x-value
    """

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        """
        class constructor

        parameters:
            data [list]: data to be used to estimate the distibution
            mean [float]: the mean of the distribution
            stddev [float]: the standard deviation of the distribution

        Sets the instance attributes mean and stddev as floats
        If data is not given:
            Use the given mean and stddev
            raise ValueError if stddev is not positive value
        If data is given:
            Calculate the mean and stddev of data
            Raise TypeError if data is not a list
            Raise ValueError if data does not contain
            at least two data points
        """
        if data is None:

