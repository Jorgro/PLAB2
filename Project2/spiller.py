""" Modul for superklassen Spiller. """

import abc
import random
from aksjon import Aksjon


""" Klassen Spiller. """


class Spiller:

    __metaclass__ = abc.ABCMeta

    stein = Aksjon("stein")
    saks = Aksjon("saks")
    papir = Aksjon("papir")

    aksjoner = [stein, saks, papir]

    def __init__(self):
        self.spiller_historie = []
        self.andre_spiller_historie = []
        self.poeng = 0

    @abc.abstractmethod
    def velg_aksjon(self):
        return

    def motta_resultat(self, selv_valgt, andre_valgt, poeng):
        self.spiller_historie.append(selv_valgt.aksjon)
        self.andre_spiller_historie.append(andre_valgt.aksjon)
        self.poeng += poeng

    def oppgi_navn(self):
        return type(self).__name__

    @staticmethod
    def finn_kompliment(aksjon, aksjoner):
        for i in aksjoner:
            if i.aksjon == aksjon:
                return Aksjon(i.kompliment)
        return None

    @staticmethod
    def finn_beste_aksjon(dictionary, aksjoner):
        mest_spilt = []

        for key, value in dictionary.items():
            if mest_spilt:
                if value > mest_spilt[0][1]:
                    mest_spilt = [(key, value)]
                elif value == mest_spilt[0][1]:
                    mest_spilt.append((key, value))
            else:
                mest_spilt.append((key, value))

        # print(dictionary)
        # print(mest_spilt)
        # print(self.andre_spiller_historie)

        if len(mest_spilt) > 1:
            aksjon = random.choice(mest_spilt)[0]
            return Spiller.finn_kompliment(aksjon, aksjoner)

        return Spiller.finn_kompliment(mest_spilt[0][0], aksjoner)
