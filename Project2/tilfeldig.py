""" Modul for tilfeldig spiller"""

import random
from spiller import Spiller


class Tilfeldig(Spiller):
    """ Klasse for tilfeldige valg av stein, saks papir. """

    def velg_aksjon(self):
        """ Velger et tilfeldig valg fra aksjoner. """

        return random.choice(Spiller.aksjoner)


