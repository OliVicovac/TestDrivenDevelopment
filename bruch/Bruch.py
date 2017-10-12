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
        """

        Rechnet absouluten Wert des Bruchs aus

        """
        return self.zaehler / self.nenner

    def __add__(self, other):
        """

        Addiert other und self
        :raise TypeError: Bei nicht int oder Bruch
        :param other: Objekt das addiert wird
        :return: addierter Bruch als float

        """
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
        """

        Addiert other und self
        :param other: Objekt das addiert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: addierter Bruch als float

        """
        if isinstance(other, Bruch):
            return self.calc() + other.calc()
        if isinstance(other, int):
            return self.calc() + other

        raise TypeError("Falscher type")

    def __eq__(self, other):
        """

        Dient zum Vergleich und gibt Boolean zurück
        :param other:Objekt, dass verglichen wird
        :return:Wenn beide Objekte gleich sind: True, wenn nicht: False

        """
        return self.calc() == other

    def __radd__(self, other):
        """

        Wenn other auf der linken Seite des Operators steht, wird diese Methode ausgeführt
        :param other: addiertes Objekt
        :return: addierter Bruch als float

        """
        if isinstance(other, int):
            return self.calc() + other

    def __truediv__(self, other):
        """

        Dividiert other und self
        :param other: Objekt das dividiert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: dividierter Bruch als float

        """
        if isinstance(other, Bruch):
            return self.calc() / other.calc()
        elif isinstance(other, int):
            return self.calc() / other
        else:
            raise TypeError("Falscher type")

    def __rtruediv__(self, other):
        """

        Wenn other auf der linken Seite des Operators steht, wird diese Methode ausgeführt
        :param other: Objekt das dividiert wird
        :raise TypeError: Bei nicht int
        :raise ZeroDivisionError: wenn der zaehler 0 ist
        :return: dividierter Bruch als float

        """
        if self.zaehler == 0:
            raise ZeroDivisionError
        if isinstance(other, int):
            return self.calc() / other
        else:
            raise TypeError("Falscher typ")


    def __itruediv__(self, other):
        """

        Wenn other auf der linken Seite des Operators steht, wird diese Methode ausgeführt
        :param other: Objekt das dividiert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: dividierter Bruch als float

        """
        if isinstance(other, Bruch):
            return self.calc() / other.calc()
        elif isinstance(other, int):
            return self.calc() / other
        else:
            raise TypeError("Falscher Typ")


    def __mul__(self, other):
        """

        Multipliziert other und self
        :param other: Objekt das multipliziert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: multiplizierter Bruch als float

        """
        if isinstance(other, Bruch):
            return self.calc() * other.calc()
        elif isinstance(other, int):
            return self.calc() * other
        else:
            raise TypeError("Falscher type")

    def __rmul__(self, other):
        """

        Wenn other auf der linken Seite des Operators steht, wird diese Methode ausgeführt
        :param other: Objekt das multipliziert wird
        :return: multiplizierter Bruch als float

        """
        if isinstance(other, int):
            return self.calc() * other

    def __imul__(self, other):
        """

        wird bei *= aufgerufen
        :param other: Objekt das multipliziert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: multiplizierter Bruch als float

        """
        if isinstance(other, int):
            return self.calc() * other
        elif isinstance(other, Bruch):
            return self.calc() * other.calc()
        else:
            raise TypeError("Falscher typ")

    def __sub__(self, other):
        """

        Subtrahiert other und self
        :param other: Objekt das subtrahiert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: subtrahierter Bruch als float

        """

        if isinstance(other, Bruch):
            return self.calc() - other.calc()
        elif isinstance(other, int):
            return self.calc() - other
        else:
            raise TypeError("Falscher type")

    def __rsub__(self, other):
        """

        Wenn other auf der linken Seite des Operators steht, wird diese Methode ausgeführt
        :param other: subtrahiertes Objekt
        :raise TypeError: Bei nicht int
        :return: subtrahierter Bruch als float

        """

        if isinstance(other, int):
            return  other - self.calc()
        raise TypeError("Falscher type")

    def __isub__(self, other):
        """

        wird bei -= aufgerufen
        :param other: Objekt das subtrahiert wird
        :raise TypeError: Bei nicht int oder Bruch
        :return: subtrahierter Bruch als float

        """

        if isinstance(other, Bruch):
            return self.calc() - other.calc()
        elif isinstance(other, int):
            return self.calc() - other
        else:
            raise TypeError("Falscher type")

    def __str__(self):
        """

        :return: Bruch als String

        """
        return '({}/{})'.format(abs(self.zaehler), abs(self.nenner))

    def __ge__(self, other):
        """
        vergleicht mit >=
        :param other: Objekt mit dem self verglichen wird
        :return: True wenn größer gleich als other, wenn nicht: False

        """
        return self.calc() >= other.calc()

    def __gt__(self, other):
        """
        vergleicht mit >
        :param other: Objekt mit dem self verglichen wird
        :return: True wenn grö?er als other, wenn nicht: False

        """
        return self.calc() > other.calc()

    def __abs__(self):
        """
        Rechnet den Betrag
        :return: Betrag von self

        """
        return abs(self.calc())

    def __float__(self):
        """

        :return: ausgerechneter float wird zurückgegeben

        """
        return self.calc()

    def __neg__(self):
        """

        :return: negativen Bruch

        """
        return Bruch(-self.zaehler, self.nenner)

    def __int__(self):
        """

        :return: einen int Wert

        """
        return int(self.calc())




