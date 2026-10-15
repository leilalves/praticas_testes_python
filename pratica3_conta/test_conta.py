"""Testes da PRÁTICA 3 — conceitos: FIXTURE, estado, exceção própria.

Rode:  pytest -v
"""
import pytest

from conta import ContaBancaria, SaldoInsuficienteError


# ---------------------------------------------------------------------------
# FIXTURE = "receita" de preparação reutilizável.
# O pytest chama a fixture automaticamente quando um teste a pede como
# parâmetro. Cada teste recebe uma conta NOVA, então um teste nunca
# contamina o outro (isolamento!).
# ---------------------------------------------------------------------------
@pytest.fixture
def conta():
    return ContaBancaria("Ana", saldo_inicial=100)


@pytest.fixture
def destino():
    return ContaBancaria("Bia")  # saldo inicial 0


# ---------------------------- depósito -------------------------------------
def test_deposito_aumenta_o_saldo(conta):
    conta.depositar(50)
    assert conta.saldo == 150


@pytest.mark.parametrize("valor_invalido", [0, -10])
def test_deposito_invalido_levanta_erro(conta, valor_invalido):
    with pytest.raises(ValueError):
        conta.depositar(valor_invalido)


# ------------------------------ saque --------------------------------------
def test_saque_diminui_o_saldo(conta):
    conta.sacar(30)
    assert conta.saldo == 70


def test_sacar_exatamente_o_saldo_zera_a_conta(conta):
    # BORDA: sacar tudo o que existe é permitido.
    conta.sacar(100)
    assert conta.saldo == 0


def test_saque_maior_que_o_saldo_e_recusado_e_nao_altera_nada(conta):
    with pytest.raises(SaldoInsuficienteError):
        conta.sacar(100.01)       # BORDA: 1 centavo acima do saldo
    # Teste de "efeito colateral": a falha não pode ter mexido no saldo.
    assert conta.saldo == 100


# ---------------------------- transferência --------------------------------
def test_transferencia_move_o_dinheiro_entre_contas(conta, destino):
    conta.transferir(destino, 40)
    assert conta.saldo == 60
    assert destino.saldo == 40


def test_transferencia_sem_saldo_nao_credita_o_destino(conta, destino):
    with pytest.raises(SaldoInsuficienteError):
        conta.transferir(destino, 500)
    # Nem saiu dinheiro de uma, nem entrou na outra.
    assert conta.saldo == 100
    assert destino.saldo == 0


# ---------------------------- histórico e encapsulamento --------------------
def test_historico_registra_as_operacoes_em_ordem(conta):
    conta.depositar(10)
    conta.sacar(5)
    assert conta.historico == [("deposito", 10), ("saque", 5)]


def test_saldo_nao_pode_ser_alterado_diretamente(conta):
    # "saldo" é uma property sem setter: atribuir direto gera AttributeError.
    with pytest.raises(AttributeError):
        conta.saldo = 1_000_000


def test_saldo_inicial_negativo_e_recusado():
    with pytest.raises(ValueError):
        ContaBancaria("Cris", saldo_inicial=-1)
