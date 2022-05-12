import abc

class Funcionario(abc.ABC):

    __slots__ = ["_nome", "_cpf", "_salario"]

    def __init__(self, nome, cpf, salario):
        self._nome    = nome
        self._cpf     = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        pass