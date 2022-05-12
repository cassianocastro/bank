import Conta

class Conta_poupanca(Conta):

    def __init__(self, numero, cliente, saldo, limite):
        super().__init__(numero, cliente, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (3 * taxa)

        return self._saldo