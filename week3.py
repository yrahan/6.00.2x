# Problem 3
def stdDevOfLengths(L):
    if L:
        n = len(L)
        u = len(''.join(L)) / float(n)
        tmp = 0
        for s in L:
            tmp += (len(s) - u) ** 2

        return (tmp / n) ** 0.5
    else:
        return float('NaN')


def stdVariation(X):
    n = len(X)
    mean = sum(X) / float(len(X))
    tmp = 0
    for x in X:
        tmp += (x - mean) ** 2
    return ((tmp / n) ** 0.5) / mean
