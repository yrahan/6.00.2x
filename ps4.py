# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    # TreatedPatient parameters
    numViruses = 100
    maxPop = 1000
    # ResistantVirus parameters
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    # average number of viruses given by simulations
    delay = 75
    treatementTime = 150
    times = range(delay + treatementTime)
    drug = 'guttagonol'
    viruses_final = [0] * numTrials
    ##viruses_sum = [0] * numTrials
    ##viruses_resistant_sum = [0] * numTrials
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb,
                                  resistances, mutProb)
                   for v in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for time in times:
            if time == delay:
                patient.addPrescription(drug)
            viruses_final[trial] = patient.update()
            ##viruses_sum[time] += patient.update()
            ##viruses_resistant_sum[time] += patient.getResistPop([drug])

    pylab.hist(viruses_final)
    ##pylab.hist(viruses_final, bins=20)
    pylab.show()

    ##viruses_avg = [vsum / float(numTrials) for vsum in viruses_sum]
    ##viruses_resistant_avg = [vsum / float(numTrials)
    ##                         for vsum in viruses_resistant_sum]
    # print viruses_avg
    # print viruses_resistant_avg
    # plotting
    ## pylab.plot(times, viruses_avg, label="Total")
    ##pylab.plot(times, viruses_resistant_avg, label="Resistant viruses")
    ##pylab.title("ResistantVirus simulation")
    ##pylab.legend("Average number of viruses")
    ##pylab.xlabel("time step")
    ##pylab.ylabel("# viruses")
    ##pylab.show()
    # TODO






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
