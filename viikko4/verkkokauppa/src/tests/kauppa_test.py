import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        def saldo(tuote_id):
            saldot = {1: 10, 2: 5, 3: 0}
            return saldot.get(tuote_id, 0)

        def hae_tuote(tuote_id):
            tuotteet = {
                1: Tuote(1, "maito", 5),
                2: Tuote(2, "leipä", 3),
                3: Tuote(3, "kahvi", 10)
            }
            return tuotteet.get(tuote_id)

        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote

        self.kauppa = Kauppa(self.varasto_mock,
                             self.pankki_mock,
                             self.viitegeneraattori_mock)

    def test_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 5
        )

    def test_tilisiirto_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 8
        )

    def test_tilisiirto_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 10
        )

    def test_tilisiirto_toinen_tuote_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 5
        )

    def test_aloita_asiointi_nollaa_ostoksen(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "11111", ANY, 5
        )

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("liisa", "22222")

        self.pankki_mock.tilisiirto.assert_called_with(
            "liisa", ANY, "22222", ANY, 3
        )

    def test_jokainen_maksu_pyytaa_uuden_viitenumeron(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.return_value = 43
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("liisa", "99999")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_poista_korista_toimii_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "11111")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "11111", ANY, 3
        )
