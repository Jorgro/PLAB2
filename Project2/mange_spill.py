import numpy as np
import matplotlib.pyplot as plt
from enkelt_spill import EnkeltSpill
from historiker import Historiker
from mest_vanlig import MestVanlig
from sekvensiell import Sekvensiell


class MangeSpill:

    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill
        self.resultater = []

    def arranger_turnering(self):

        for i in range(1, self.antall_spill + 1):
            spill = EnkeltSpill(self.spiller1, self.spiller2)
            spill.gjennomfoer_spill()
            print(spill)
            self.resultater.append(
                (self.spiller1.poeng, self.spiller2.poeng, i))
            print(self.resultater)
        self.plott_graf()

    def plott_graf(self):
        x_axis = np.arange(1, self.antall_spill + 1, 1)
        y_1_axis = np.zeros(self.antall_spill)
        y_2_axis = np.zeros(self.antall_spill)

        index = 0
        for i in self.resultater:
            y_1_axis[index] = i[0] / i[2]
            y_2_axis[index] = i[1] / i[2]
            index += 1

        plt.plot(x_axis, y_1_axis, label='Spiller 1')
        #plt.plot(x, y2, label='Spiller 2')

        plt.show()


TURNERING = MangeSpill(Historiker(2), Sekvensiell(), 100)
TURNERING.arranger_turnering()
