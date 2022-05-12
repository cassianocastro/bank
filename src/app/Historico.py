import datetime

class Historico:

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes    = []

    def imprime(self):
        print("Data de abertura: {}\nTransações: ".format(self._data_abertura))

        for t in self._transacoes:
            print(" - ", t)