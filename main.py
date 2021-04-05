import tkinter as tk
from tkinter import *
from tkinter import ttk

import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import nadson

# Definindo interface
janela_principal = tk.Tk()

DPI = janela_principal.winfo_fpixels("1i")

janela_principal.title("Gestão de Custos")
janela_principal.resizable(True, True)
janela_principal.config(bg="#cfcfcf")
janela_principal.resizable(0, 0)

largura_janela = janela_principal.winfo_screenwidth()
altura_janela = janela_principal.winfo_screenheight()

janela_principal.geometry("%dx%d+0+0" % (largura_janela, altura_janela))

largura_grafico = largura_janela * 0.95
altura_grafico = altura_janela * 0.85
figura = Figure(figsize=(largura_grafico / DPI, altura_grafico / DPI), dpi=DPI)
figura.patch.set_facecolor("#cfcfcf")
graficos = figura.subplots(2)

canvas = FigureCanvasTkAgg(figura, janela_principal)
canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


variacao = 1
indice = np.arange(variacao)
largura_barra = 0.09
lucros = nadson.calcula_custos()
media_lucro = nadson.media_lucro()
media_lucro_baixa_ocorrencia = nadson.media_lucro_baixa_ocorrencia()
media_lucro_media_ocorrencia = nadson.media_lucro_media_ocorrencia()
media_lucro_alta_ocorrencia = nadson.media_lucro_alta_ocorrencia()

# Definindo o grafico de barra
graficos[0].bar(
    indice + largura_barra + largura_barra,
    media_lucro_baixa_ocorrencia,
    largura_barra,
    color="#07079c",
    label=f"Baixa:{media_lucro_baixa_ocorrencia}",
)
graficos[0].bar(
    indice + largura_barra + largura_barra + largura_barra + largura_barra,
    media_lucro_media_ocorrencia,
    largura_barra,
    color="#c91509",
    label=f"Média: {media_lucro_media_ocorrencia}",
)
graficos[0].bar(
    indice
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra,
    media_lucro_alta_ocorrencia,
    largura_barra,
    color="#078906",
    label=f"Alta: {media_lucro_alta_ocorrencia}",
)
graficos[0].bar(
    indice
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra
    + largura_barra,
    media_lucro,
    largura_barra,
    color="#f5bf14",
    label=f"Total: {media_lucro}",
)

graficos[1].plot(
    range(1000),
    lucros,
    color="#c91509",
    label="Média",
)

# Grafico de Barra
graficos[0].set_ylim(0, 350)
graficos[0].set_title("Probabilidades de Ocorrência", fontweight="bold")
graficos[0].set_xticks(indice + largura_barra)
graficos[0].legend()
graficos[0].grid(True)


# Grafico de variação de saldo
graficos[1].set_title("Variação de Saldo", fontweight="bold")
graficos[1].grid(True)



def calcular():
    lucros = nadson.calcula_custos()


janela_principal.mainloop()
