import math
import random


def exponential_distribution():
    '''
    Generate a random variable that follows an exponential distribution.

    The exponential distribution models the time between events in a Poisson point process, 
    i.e., a process in which events occur continuously and independently at a constant average rate.

    Returns:
    float: A random variable that follows an exponential distribution.
    '''
    num = 0.05 + 0.45 * random.random()
    return -math.log(1.0 - random.random()) / num


def weibull_distribution(k=0):
    '''
    Generate a random variable that follows a Weibull distribution.

    The Weibull distribution is a generalization of the exponential distribution that 
    models the time to failure analysis. It can model a variety of shapes of the 
    failure rate function.

    Parameters:
    k (float): The shape parameter. Must be greater than -1.
    If k = 0, the Weibull distribution becomes an exponential distribution.
    If k < 0, the failure rate decreases over time.
    If k > 0, the failure rate increases over time.
    The shape parameter represent how the repair time changes over time.

    Returns:
    float: A random variable that follows a Weibull distribution.
    '''
    k += 1
    num = 30 + 90 * random.random()
    return num * ((-math.log(1.0 - random.random())) ** (1 / k))