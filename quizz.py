import numpy
import random
import pylab

def sampleQuizzes():
    # Your code here
    numTrials = 100000
    yes = 0
    for trial in range(numTrials):
        midterm1 = random.randrange(50, 81)
        midterm2 = random.randrange(60, 91)
        finalExam = random.randrange(55, 96)
        grade = 0.25 * (midterm1 + midterm2) + 0.50 * finalExam
        if grade >= 70 and grade <= 75:
            yes += 1
    return yes / float(numTrials)


def probTest(limit):
    rolls = 0
    while (1 / 6.0) * (5 / 6.0) ** rolls >= limit:
        rolls += 1
    return rolls + 1


def runLV(k):
    # generate balls
    whiteBalls = random.sample(range(1000), 500)
    numTrials = 100000
    histogram = [0] * 1000
    for i in range(numTrials):
        j = 1
        while(j <= k and random.randrange(1000) not in whiteBalls):
            j += 1
        histogram[j] += 1
    pylab.figure(1)
    pylab.plot(range(1000), histogram)
    pylab.title("Title")
    pylab.xlabel("X")
    pylab.ylabel("Y")
    pylab.show()
