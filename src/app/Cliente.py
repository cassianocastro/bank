
class Cliente:

	def __init__(self, nome, sobrenome, cpf):
		self.nome      = nome
		self.sobrenome = sobrenome
		self.cpf       = cpf

if __name__ == "__main__":
    import Conta

    cliente     = Cliente("Cassiano", "Rodrigues", "123456789")
    minha_conta = Conta("123-4", cliente, 120.0, 1000.0)