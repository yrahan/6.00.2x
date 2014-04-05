import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here

    yes = 0.0
    for i in range(numTrials):
        bucket = ['r', 'r', 'r', 'g', 'g', 'g']
        trial = []
        for j in range(3):
            trial.append(random.choice(bucket))
            bucket.remove(trial[j])
        if (trial[0] == trial[1]) and (trial[1] == trial[2]):
            yes += 1
    return yes / float(numTrials)
