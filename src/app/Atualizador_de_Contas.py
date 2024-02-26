
class Atualizador_contas:

    def __init__(self, selic, saldo_total):
        self._selic       = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo da conta: {}".format(conta.saldo))

        self._saldo_total += conta.atualiza(self._selic)

        print("Saldo final: {}".format(self._saldo_total))