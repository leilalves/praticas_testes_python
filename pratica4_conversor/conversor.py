"""PRÁTICA 4 — Conversor de temperatura (LÓGICA, sem nenhuma tela).

Regra de ouro para testar programas desktop: deixe a lógica em arquivos que
NÃO importam tkinter. Assim ela é testada em milissegundos, sem abrir janela.
"""

ZERO_ABSOLUTO_C = -273.15


def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def converter_texto(texto):
    """Recebe o TEXTO digitado pelo usuário e devolve o texto do resultado.

    Aceita vírgula decimal ("36,5"). Levanta ValueError (com mensagem amigável)
    se não for número ou se estiver abaixo do zero absoluto.
    """
    limpo = texto.strip().replace(",", ".")
    try:
        celsius = float(limpo)
    except ValueError:
        raise ValueError("Digite um número válido.") from None

    if celsius < ZERO_ABSOLUTO_C:
        raise ValueError("Temperatura abaixo do zero absoluto (-273,15 °C).")

    return f"{celsius_para_fahrenheit(celsius):.1f} °F"
