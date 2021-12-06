class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self._edellinen_tulos = 0

    def miinus(self, arvo):
        self._edellinen_tulos = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self._edellinen_tulos = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self._edellinen_tulos = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
    
    def kumoa(self):
        self.tulos = self._edellinen_tulos
