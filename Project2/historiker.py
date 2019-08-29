from spiller import Spiller


class Historiker(Spiller):

    def __init__(self, husk=1):
        super().__init__()
        self.husk = husk

    def velg_aksjon(self):
        dictionary = self.subfinder()
        return Spiller.finn_beste_aksjon(dictionary, self.aksjoner)

    def subfinder(self):
        dictionary = {"stein": 0, "saks": 0, "papir": 0}

        if len(self.andre_spiller_historie) <= self.husk:
            return dictionary

        sekvens = self.andre_spiller_historie[len(
            self.andre_spiller_historie) - self.husk:len(self.andre_spiller_historie)]

        print(sekvens)

        for i in range(len(self.andre_spiller_historie)):
            if (self.andre_spiller_historie[i] == sekvens[0]
                    and self.andre_spiller_historie[i:i + len(sekvens)] == sekvens):
                if i + self.husk < len(self.andre_spiller_historie):
                    dictionary[self.andre_spiller_historie[i + self.husk]] += 1

        return dictionary
