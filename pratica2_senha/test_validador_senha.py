"""Testes da PRÁTICA 2 — conceitos: tabela de casos, borda e CAÇA AO BUG.

Rode:  pytest -v
Resultado esperado NA PRIMEIRA EXECUÇÃO: 1 teste FALHA (de propósito).
Missão: descobrir o porquê, registrar o defeito, corrigir e rodar de novo.
"""
import pytest

from validador_senha import senha_valida, validar_senha


# ---------------------------------------------------------------------------
# Caminho feliz: uma senha longa e forte não pode ter problema algum.
# ---------------------------------------------------------------------------
def test_senha_forte_nao_tem_problemas():
    assert validar_senha("Senha@Forte123") == []


# ---------------------------------------------------------------------------
# TABELA DE CASOS NEGATIVOS: cada linha quebra UMA regra de propósito e
# conferimos se a mensagem certa aparece. Se amanhã alguém mudar uma regra,
# o teste mostra exatamente qual linha parou de funcionar.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "senha, trecho_da_mensagem",
    [
        ("Abc1!", "no mínimo 8"),         # curta demais
        ("abcdefg1!", "maiúscula"),       # sem maiúscula
        ("ABCDEFG1!", "minúscula"),       # sem minúscula
        ("Abcdefgh!", "dígito"),          # sem número
        ("Abcdefg12", "símbolo"),         # sem símbolo
        ("Abcd 1234!", "espaço"),         # com espaço
    ],
)
def test_cada_regra_quebrada_gera_sua_mensagem(senha, trecho_da_mensagem):
    problemas = validar_senha(senha)
    # any(...) = "existe ao menos uma mensagem que contém esse trecho?"
    assert any(trecho_da_mensagem in p for p in problemas)


# ---------------------------------------------------------------------------
# VALOR LIMITE: o tamanho mínimo é 8. Testamos 7 (inválido), 8 (a borda!)
# e 9 (válido). Todas têm maiúscula, minúscula, dígito e símbolo, então a
# ÚNICA coisa que muda é o tamanho.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "senha, esperado",
    [
        ("Abcde1!", False),     # 7 caracteres
        ("Abcdef1!", True),     # 8 caracteres  <- a borda
        ("Abcdefg1!", True),    # 9 caracteres
    ],
)
def test_tamanho_minimo_na_borda(senha, esperado):
    assert senha_valida(senha) is esperado


# ---------------------------------------------------------------------------
# Várias regras quebradas ao mesmo tempo: o usuário deve ver TODOS os
# problemas de uma vez, não um por tentativa. Senha vazia quebra 5 regras.
# ---------------------------------------------------------------------------
def test_senha_vazia_acumula_todos_os_problemas():
    assert len(validar_senha("")) == 5
