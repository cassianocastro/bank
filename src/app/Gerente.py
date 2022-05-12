import Funcionario

class Gerente(Funcionario):

    __slots__ = ["_nome", "_cpf", "_salario", "_senha", "_qtd_funcionarios"]

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha            = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if (self._senha == senha):
            print("Acesso Permitido")
            return True
        else:
            print("Acesso Negado")
            return False

    def get_bonificacao(self):
        return self._salario * 0.15