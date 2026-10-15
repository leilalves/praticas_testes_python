"""PRÁTICA 3 — Conta bancária (classe com ESTADO).

Diferente das funções puras, aqui o objeto "lembra" o saldo. Os testes
precisam preparar o objeto antes — é para isso que existem as FIXTURES.
"""


class SaldoInsuficienteError(Exception):
    """Exceção própria: deixa o erro claro e fácil de testar."""


class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.titular = titular
        self._saldo = saldo_inicial   # "_" = uso interno (encapsulamento)
        self.historico = []           # lista de tuplas: (operação, valor)

    @property
    def saldo(self):
        """Somente leitura: só depositar/sacar/transferir alteram o saldo."""
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor
        self.historico.append(("deposito", valor))

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo:
            # Importante: validamos ANTES de mexer no saldo.
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        self._saldo -= valor
        self.historico.append(("saque", valor))

    def transferir(self, destino, valor):
        """Tira da conta atual e coloca na conta de destino."""
        self.sacar(valor)          # se faltar saldo, levanta erro e PARA aqui
        destino.depositar(valor)   # só chega aqui se o saque deu certo
