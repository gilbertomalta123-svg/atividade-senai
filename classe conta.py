class Conta:
    def __init__(self,saldo):
        self._saldo=saldo
    def get_saldo(self):
        print(f"o seu saldo de conta e de {self._saldo}")
    def depositar(self,valor):
        self.valor=valor
        self._saldo+=valor

gilberto=Conta(100000)

gilberto.depositar(500)
gilberto.get_saldo()