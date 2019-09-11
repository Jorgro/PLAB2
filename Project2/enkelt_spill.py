#from tilfeldig import Tilfeldig
#from sekvensiell import Sekvensiell
#from mest_vanlig import MestVanlig
import test
from historiker import Historiker


class EnkeltSpill:

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.resultat = ""
        self.valg1 = None
        self.valg2 = None

    def gjennomfoer_spill(self):
        self.valg1 = self.spiller1.velg_aksjon()
        self.valg2 = self.spiller2.velg_aksjon()
        
        if self.valg1 == self.valg2:
            self.spiller1.motta_resultat(self.valg1, self.valg2, 0.5)
            self.spiller2.motta_resultat(self.valg2, self.valg1, 0.5)
            self.resultat = "Uavgjort."

        elif self.valg1 > self.valg2:
            self.spiller1.motta_resultat(self.valg1, self.valg2, 1)
            self.spiller2.motta_resultat(self.valg2, self.valg1, 0)
            self.resultat = "" + str(self.spiller1) + " vant."

        else:
            self.spiller1.motta_resultat(self.valg1, self.valg2, 0)
            self.spiller2.motta_resultat(self.valg2, self.valg1, 1)
            self.resultat = "" + str(self.spiller2) + " vant."

    def __str__(self):

        tekst = f'{self.spiller1.oppgi_navn()} valgte {self.valg1}. '\
                f'{self.spiller2.oppgi_navn()} valgte {self.valg2}. {self.resultat}'
        return tekst


SPILLER_1 = Historiker(3)
SPILLER_2 = test.Test()

for i in range(len(test.Test.test_sekvens.split(", "))):
    spill = EnkeltSpill(SPILLER_1, SPILLER_2)

    spill.gjennomfoer_spill()
    print(spill)
