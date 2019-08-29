""" Modul for test klassen."""

from spiller import Spiller
from aksjon import Aksjon


class Test(Spiller):

    """ Klassen Test, hvor man setter inn en egen streng som spilles. """
    test_sekvens = (
        "stein, saks, stein, "
        "stein, papir, saks, papir, stein, papir, stein, stein, saks, papir, saks, stein")

    def __init__(self):
        super().__init__()
        self.index = 0

    def velg_aksjon(self):
        liste = Test.test_sekvens.split(", ")
        aksjon = Aksjon(liste[self.index])
        self.index += 1
        return aksjon
