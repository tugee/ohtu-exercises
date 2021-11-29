from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavaroita = 0
        self._hinta = 0
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self.tavaroita += 1
        self._hinta += lisattava.hinta()

        match = False
        for ostos in self.ostokset():
            if ostos.tuotteen_nimi() == lisattava.nimi():
               ostos.muuta_lukumaaraa(1)
               match = True
        
        if not match:
           self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        self.tavaroita -= 1
        self._hinta -= poistettava.hinta()
        ostokset = self.ostokset()

        for ostos in ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
               ostos.muuta_lukumaaraa(-1)
               if ostos.lukumaara() == 0:
                  ostokset.remove(ostos)


    def tyhjenna(self):
        self.tavaroita = 0
        self._hinta = 0
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
