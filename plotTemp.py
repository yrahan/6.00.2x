# The goal of this exercise is to produce a plot that shows the difference
# between the high and the low temperature for each day.
import pylab
from numpy import array


def getMinMaxTemp(filename):
    # y1 data
    minTemps = []
    # y2 data
    maxTemps = []
    # parse and get min and max temperatures from a text file
    with open(filename, 'r') as inFile:
        for line in inFile:
            fields = line.split()
            if not(len(fields) != 3 or 'Boston' == fields[0] or
                   'Day' == fields[0]):
                minTemps.append(int(fields[2]))
                maxTemps.append(int(fields[1]))
        return (minTemps, maxTemps)


def producePlot(filename):
    lowTemps, highTemps = getMinMaxTemp(filename)
    pylab.figure(1)
    diffTemps = array(highTemps) - array(lowTemps)
    pylab.plot(range(1, 1 + diffTemps.size), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.savefig('figure-Temperature-Boston-July-2012')
    #pylab.show()


def main():
    filename = 'julyTemps.txt'
    producePlot(filename)

if __name__ == "__main__":
        main()
