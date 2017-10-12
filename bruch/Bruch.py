"""
Created on 18.09.2017

@author: Michael Borko <mborko@tgm.ac.at>
@version: 20170918

@description: Implementierung einiger Operationen, um das Rechnen mit Bruechen zu ermoeglichen
"""

class Bruch(object):

    """
    Konstruktor
    :type zaehler: Zaehler des Bruchs
    :type nenner: Nenner des Bruchs
    """
    def __init__(self, zaehler=None, nenner=None):
        # Klassenaufruf: Bruch(2,4)
        if isinstance(zaehler, int) and isinstance(nenner, int):
            # --> Division durch 0 ueberpruefen
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            elif zaehler < 0 and nenner < 0:
                self.zaehler = abs(zaehler)
                self.nenner = abs(nenner)
            else:
                raise ZeroDivisionError("Division durch 0 nicht definiert!")

        # Klassenaufruf: self.b2 = Bruch(self.b)
        # --> Zuweisen von Zaehler und Nenner aus dem Bruchobjekt
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

        # Klassenaufruf: Bruch(4)
        # --> ohne Nenner, daher Deklarierung von Nenner = 1
        elif isinstance(zaehler, int) and not isinstance(nenner, float):
            self.zaehler = zaehler
            self.nenner = 1
        else:
            raise TypeError("Zaehler und/oder Nenner nicht zulaessig!")

    """
    Ergänzung durch ovicovac
    """

    def calc(self):
        return self.zaehler / self.nenner

    def __add__(self, other):
        if isinstance(other, Bruch):
            return self.calc() + other.calc()
        elif isinstance(other, int):
            return self.calc() + other
        else:
            raise TypeError("Falscher type")

    def __float__(self):
        print("__float__ was called")
        pass

    def __iadd__(self, other):
        if isinstance(other, Bruch):
            return self.calc() + other.calc()
        elif isinstance(other, int):
            return self.calc() + other
        else:
            raise TypeError("Falscher type")

    def __eq__(self, other):
        return self.calc() == other

    def __radd__(self, other):
        if isinstance(other, int):
            return self.calc() + other

    def __truediv__(self, other):
        if isinstance(other, Bruch):
            return self.calc() / other.calc()
        elif isinstance(other, int):
            return self.calc() / other
        else:
            raise TypeError("Falscher type")

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return self.calc() / other
        raise TypeError("Falscher type")

    def __mul__(self, other):
        if isinstance(other, Bruch):
            return self.calc() * other.calc()
        elif isinstance(other, int):
            return self.calc() * other
        else:
            raise TypeError("Falscher type")

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.calc() * other

    def __imul__(self, other):
       if isinstance(other, int):
           return self.calc() * other
       elif isinstance(other, Bruch):
           return self.calc() * other.calc()
       else:
           raise TypeError("Falscher typ")

    def __sub__(self, other):
        if isinstance(other, Bruch):
            return self.calc() - other.calc()
        elif isinstance(other, int):
            return self.calc() - other
        else:
            raise TypeError("Falscher type")

    def __rsub__(self, other):
        if isinstance(other, int):
            return self.calc() - other




