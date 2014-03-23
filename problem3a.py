import random


def deterministicNumber():
    '''
    Deterministically generates and return an even number between 9 and 21.
    '''

    random.seed(10)
    return random.randrange(9, 21, 2)
