# The goal of this exercise is to produce a plot that shows the difference
# between the high and the low temperature for each day.
#import pylab


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
                minTemps.append(int(fields[1]))
                maxTemps.append(int(fields[2]))
        return (minTemps, maxTemps)


def main():
    filename = 'julyTemps.txt'
    minTemps, maxTemps = getMinMaxTemp(filename)
    print minTemps, maxTemps

if __name__ == "__main__":
        main()
