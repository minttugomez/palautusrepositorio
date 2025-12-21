from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def pelaa(self, gamemode):
        tuomari = Tuomari()
        tekoaly = Tekoaly()
        tekoaly2 = TekoalyParannettu(10)

        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            if gamemode == "a":
                tokan_siirto = input("Toisen pelaajan siirto: ")
            elif gamemode == "b":
                tokan_siirto = tekoaly.anna_siirto()
                print(f"Tietokone valitsi: {tokan_siirto}")
            elif gamemode == "c":
                tokan_siirto = tekoaly2.anna_siirto()
                print(f"Tietokone valitsi: {tokan_siirto}")
            if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(tokan_siirto):
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
