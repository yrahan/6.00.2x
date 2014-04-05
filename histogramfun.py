import pylab


#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
# You may have to change this path
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """

    vals = []
    vowels = 'aeiou'
    for w in wordList:
        vals.append(sum({vowel: w.count(vowel) for vowel in vowels}.values())
                    / float(len(w)))
    pylab.hist(vals, numBins)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    print 'x-range =', xmin, '-', xmax
    print 'y-range =', ymin, '-', ymax
    pylab.figure
    ##pylab.hist(vals, bins = 11)
    ###pylab.xlim(-1.0, 2.0)
    pylab.show()
    ##assert False


if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
