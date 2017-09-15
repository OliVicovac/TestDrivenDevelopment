class Bruch():
    def __init__(self, zaehler=None, nenner=None):
        if isinstance(zaehler, int) and isinstance(nenner, int):
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            else:
                raise ZeroDivisionError("Nenner darf nicht 0 sein!")
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            self.zaehler = zaehler
            self.nenner = 1
        else:
            raise TypeError("Zähler und/oder Nenner nicht zulässig!")

    def __iter__(self):
        return (self.zaehler,self.nenner).__iter__()