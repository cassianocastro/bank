
class Controle_bonificacoes:

    def __init__(self, total_bonificacoes = 0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if (hasattr(obj, "get_bonificacao")):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(
                "Instância de {} não implementa o método get_bonificacao()."
                .format (self.__class__.__name__)
            )