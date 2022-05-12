import abc
import Historico

class Conta(abc.abc):

    _total_contas  = 0
    _identificador = 0
    __slots__      = ["_numero", "_titular", "_saldo", "_limite"]

    def __init__(self, numero, cliente, saldo, limite):
        self._numero          = numero
        self._titular         = cliente
        self._saldo           = saldo
        self._limite          = limite
        self._historico       = Historico()
        self._identificador   = Conta._identificador
        Conta._identificador += 1
        Conta._total_contas  += 1

        print ("Conta criada com sucesso.")

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @abs.abstractmethod
    def atualiza(self, taxa):
        pass

    def deposita(self, valor):
        if (valor < 0):
            raise ValueError("Você tentou depositar um valor negativo!")
        else:
            self._saldo += valor
            self.historico.transacoes.append("Depósito de {} reais.".format(valor))

    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append("Saque de {} reais.".format(valor))
            return True

    def transfere_para(self, conta_destino, valor):
        retirou = self.saca(valor)

        if (retirou == False):
            return False
        else:
            conta_destino.deposita(valor)
            self._historico.transacoes.append("Tranferencia de {} para conta {}".format(valor, conta_destino.numero))
            return True

    def extrato(self):
        print ("Número: {}\nSaldo: {}" .format (self._numero, self._saldo))

        self._historico.transacoes.append("Tirou comprovante de Saldo - Saldo {}".format(self.saldo))

    def getSaldo(self):
        return self._saldo

    def setSaldo(self, saldo):
        self._saldo = saldo

    def __str__(self):
        return "Dados da conta: \nNúmero: {}\nTitular: {}\nSaldo: {}\nLimite: {}".format(self._numero, self._titular, self._limite, self._saldo)

if __name__ == "__main__":
	import Tributavel, Conta_corrente, Seguro_de_Vida, Manipulador

	cc = Conta_corrente("João", "123-4")
	cc.deposita(1000.0)

	seguro = Seguro_de_Vida(100.0, "José", "345-77")

	Tributavel.register(Conta_corrente)
	Tributavel.register(Seguro_de_Vida)

	lista_tributaveis = []
	lista_tributaveis.append(cc)
	lista_tributaveis.append(seguro)

	mt    = Manipulador()
	total = mt.calcula_impostos(lista_tributaveis)

	print(total)