"""Testes da PRÁTICA 4 — três níveis de teste para um programa desktop.
   Nível A  lógica pura            -> rápido, o MAIS importante
   Nível B  interface com dublês   -> sem janela (Mock + patch)
   Nível C  janela real            -> lento, poucos, precisa de tela
Rode:  pytest -v          (sem o nível C: pytest -v -m "not gui")
"""
import tkinter as tk
from unittest.mock import Mock, patch
import pytest
from app import AppConversor
from conversor import (
      celsius_para_fahrenheit,
      converter_texto,
      fahrenheit_para_celsius,
)
# ===========================================================================
# NÍVEL A — lógica pura (nenhuma janela envolvida)
# ===========================================================================
@pytest.mark.parametrize(
      "celsius, fahrenheit",
      [(0, 32), (100, 212), (-40, -40), (37, 98.6)],
)
def test_celsius_para_fahrenheit(celsius, fahrenheit):
      assert celsius_para_fahrenheit(celsius) == pytest.approx(fahrenheit)
def test_ida_e_volta():
      assert fahrenheit_para_celsius(celsius_para_fahrenheit(25)) == pytest.approx(25)
@pytest.mark.parametrize(
      "digitado, esperado",
      [
            ("100", "212.0 °F"),
            (" 36.5", "97.7 °F"),
            ("-273.15", "-459.7 °F"),
      ],
)
def test_converter_texto_valido(digitado, esperado):
      assert converter_texto(digitado) == esperado
@pytest.mark.parametrize(
      "digitado, trecho_do_erro",
      [
            ("abc", "número válido"),
            ("", "número válido"),
            ("-273.16", "zero absoluto"),
      ],
)
def test_converter_texto_invalido(digitado, trecho_do_erro):
      with pytest.raises(ValueError, match=trecho_do_erro):
            converter_texto(digitado)
# ===========================================================================
# NÍVEL B — interface testada SEM abrir janela
#   AppConversor.__new__(AppConversor) cria o objeto PULANDO o __init__
#   (que abriria a janela). Depois trocamos os widgets por Mock: um
#   objeto "de mentira" que aceita qualquer chamada e a registra.
# ===========================================================================
def criar_app_sem_janela(texto_digitado):
      app = AppConversor.__new__(AppConversor)  
      app.entrada = Mock()
      app.entrada.get.return_value = texto_digitado
      app.rotulo = Mock()
      return app
def test_clique_com_entrada_valida_mostra_o_resultado():
      app = criar_app_sem_janela("100")
      app.converter()
      app.rotulo.config.assert_called_once_with(text="212.0 °F")
def test_clique_com_entrada_invalida_mostra_erro_sem_quebrar():
      app = criar_app_sem_janela("abc")
      with patch("app.messagebox") as msg:
            app.converter()
            msg.showerror.assert_called_once()
            app.rotulo.config.assert_called_once_with(text="—")
# ===========================================================================
# NÍVEL C — janela REAL. Usamos botao.invoke(), que executa o "command" do
# botão sem precisar do mainloop() (que travaria o teste).
# Em computador sem tela (servidor Linux) o teste é PULADO, não falha.
# ===========================================================================
@pytest.mark.gui
def test_gui_real_clique_no_botao():
      try:
         app = AppConversor()
      except tk.TclError:
            pytest.skip("Sem ambiente gráfico")
      try:
         app.entrada.insert(0, "0")
         app.botao.invoke()
         assert app.rotulo.cget("text") == "32.0 °F"
      finally:
         app.janela.destroy()