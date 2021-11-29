import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.tavaroita_korissa(),0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3)

    def test_kahden_tuotteen_lisaaminen_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        vesi = Tuote("Vesi", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(vesi)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_tuotteen_lisaaminen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        vesi = Tuote("Vesi", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(vesi)
        self.assertEqual(self.kori.hinta(),5)

    def test_kahden_saman_tuotteen_lisaaminen_tavaroiden_maara_oikein(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_kahden_saman_tuotteen_lisaaminen_tavaroiden_maara_oikein(self):
        maito = Tuote("Maito",3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset,1)
