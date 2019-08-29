import random
from spiller import Spiller




class MestVanlig(Spiller):

    def velg_aksjon(self):
        if not self.andre_spiller_historie:
            return random.choice(Spiller.aksjoner)

        dictionary = {"stein": 0, "saks": 0, "papir": 0}

        for i in self.andre_spiller_historie:
            dictionary[i] += 1

        return Spiller.finn_beste_aksjon(dictionary, self.aksjoner)
