from spiller import Spiller


class Sekvensiell(Spiller):

    def __init__(self):
        super().__init__()
        self.index = 0

    def velg_aksjon(self):
        aksjon = Spiller.aksjoner[self.index]
        self.index += 1
        if self.index == 3:
            self.index = 0
        return aksjon
