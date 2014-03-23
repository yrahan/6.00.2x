import random


def stochasticNumber():
    '''
    Stochastically generates and returns
    a uniformaly distributed even number
    between 9 and 21
    '''

    return random.randrange(10, 20, 2)
