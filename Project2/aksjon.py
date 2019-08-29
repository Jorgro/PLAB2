class Aksjon:

    def __init__(self, aksjon):

        self.aksjon = aksjon
        self.kompliment = ""
        self.sett_kompliment()

    def __str__(self):
        return self.aksjon

    def __eq__(self, andre):
        return self.aksjon == andre.aksjon

    def __gt__(self, andre):

        if self.aksjon == "stein" and andre.aksjon == "saks":
            return True
        elif self.aksjon == "saks" and andre.aksjon == "papir":
            return True
        elif self.aksjon == "papir" and andre.aksjon == "stein":
            return True

        return False

    def sett_kompliment(self):

        if self.aksjon == "stein":
            self.kompliment = "papir"

        elif self.aksjon == "saks":
            self.kompliment = "stein"

        else:
            self.kompliment = "saks"
