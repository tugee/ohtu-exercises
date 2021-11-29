KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self):
        self.ljono = []

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono.append(n)
            return True
        return False

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        return self.ljono

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        x.ljono = a_taulu + b_taulu
        
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        y.ljono = list(set(a_taulu) & set(b_taulu))

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        z.ljono = list(set(a_taulu) - set(b_taulu))

        return z

    def __str__(self):
        if self.mahtavuus() == 0:
            return "{}"
        elif self.mahtavuus() == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.mahtavuus() - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.mahtavuus() - 1])
            tuotos = tuotos + "}"
            return tuotos
