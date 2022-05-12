import Conta

class Conta_corrente(Conta):

    _taxa_bancaria = 0.0

    def __init__(self, numero, cliente, saldo, limite):
        super().__init__(numero, cliente, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (2 * taxa)

        return self._saldo

    def deposita(self, valor):
        valor -= 0.10
        taxa_bancaria += 0.10

        self._saldo += valor
        self.historico.transacoes.append("Depósito de {} reais.".format(valor))

    def get_valor_imposto(self):
        return self._saldo * 0.01