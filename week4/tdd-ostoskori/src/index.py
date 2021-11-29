from ostoskori import Ostoskori
from tuote import Tuote

kori = Ostoskori()
maito = Tuote("Maito",3)

kori.lisaa_tuote(maito)
kori.lisaa_tuote(maito)

kori.hinta()
