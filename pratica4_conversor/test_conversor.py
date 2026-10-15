"""Testes da PRÁTICA 4 — três níveis de teste para um programa desktop.

   Nível A  lógica pura            -> rápido, o MAIS importante
   Nível B  interface com dublês   -> sem janela (Mock + patch)
   Nível C  janela real            -> lento, poucos, precisa de tela

Rode:  pytest -v          (sem o nível C: pytest -v -m "not gui")


"""



# Digitar a partir deste ponto (1º Código)



# ===========================================================================
# NÍVEL A — lógica pura (nenhuma janela envolvida)
# ===========================================================================



# Digitar código (Aqui)



# ===========================================================================
# NÍVEL B — interface testada SEM abrir janela
#   AppConversor.__new__(AppConversor) cria o objeto PULANDO o __init__
#   (que abriria a janela). Depois trocamos os widgets por Mock: um
#   objeto "de mentira" que aceita qualquer chamada e a registra.
# ===========================================================================




# Digitar código (Aqui)




# ===========================================================================
# NÍVEL C — janela REAL. Usamos botao.invoke(), que executa o "command" do
# botão sem precisar do mainloop() (que travaria o teste).
# Em computador sem tela (servidor Linux) o teste é PULADO, não falha.
# ===========================================================================



# Digitar código (Aqui)