import random


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
