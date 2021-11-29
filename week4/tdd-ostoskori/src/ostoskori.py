from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.ostokset())
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.ostokset())
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):

        match = False
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi() == lisattava.nimi():
               ostos.muuta_lukumaaraa(1)
               match = True
        
        if not match:
           self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ostokset = self.ostokset()

        for ostos in ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
               ostos.muuta_lukumaaraa(-1)
               if ostos.lukumaara() == 0:
                  ostokset.remove(ostos)


    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
