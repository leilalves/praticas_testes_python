"""PRÁTICA 1 — Boletim escolar.

Duas funções PURAS (mesma entrada => mesma saída, sem tela, sem banco, sem
arquivo). Funções puras são as mais fáceis de testar: por isso a primeira
prática começa por aqui.
"""

# Constantes com nome: evitam "números mágicos" espalhados pelo código e
# deixam as regras de negócio num lugar só.
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
MEDIA_APROVACAO = 6.0     # média >= 6  -> Aprovado
MEDIA_RECUPERACAO = 4.0   # 4 <= média < 6 -> Recuperação; abaixo -> Reprovado


def calcular_media(notas):
    """Devolve a média aritmética de uma lista de notas (0 a 10).

    Levanta ValueError se a lista estiver vazia ou se alguma nota for inválida.
    """
    if not notas:
        raise ValueError("Informe ao menos uma nota.")

    for nota in notas:
        if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
            raise ValueError(f"Nota {nota} fora do intervalo: use valores entre 0 e 10.")

    return sum(notas) / len(notas)


def situacao(media):
    """Traduz a média na situação do aluno."""
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    if media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    return "Reprovado"
