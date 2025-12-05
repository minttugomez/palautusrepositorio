class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = []

    def miinus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = arvo

    def kumoa(self):
        if self._edelliset_arvot:
            self._arvo = self._edelliset_arvot.pop(-1)

    def arvo(self):
        return self._arvo
