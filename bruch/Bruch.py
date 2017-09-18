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