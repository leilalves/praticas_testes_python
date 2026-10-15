"""PRÁTICA 4 — Interface Tkinter (FINA): só desenha e repassa para a lógica.

Para executar o programa de verdade:   python app.py
"""
import tkinter as tk
from tkinter import messagebox

from conversor import converter_texto


class AppConversor:
    def __init__(self):
        # Tudo que cria janela fica aqui. É exatamente por isso que os testes
        # unitários "pulam" o __init__ (veja test_conversor.py).
        self.janela = tk.Tk()
        self.janela.title("Conversor °C → °F")

        self.entrada = tk.Entry(self.janela, width=14)
        self.botao = tk.Button(self.janela, text="Converter", command=self.converter)
        self.rotulo = tk.Label(self.janela, text="—", font=("Arial", 16))

        for widget in (self.entrada, self.botao, self.rotulo):
            widget.pack(padx=20, pady=8)

    def converter(self):
        """Chamado pelo clique do botão: lê a tela, chama a lógica, mostra."""
        texto = self.entrada.get()
        try:
            resultado = converter_texto(texto)
        except ValueError as erro:
            messagebox.showerror("Entrada inválida", str(erro))
            self.rotulo.config(text="—")
            return
        self.rotulo.config(text=resultado)

    def executar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    AppConversor().executar()
