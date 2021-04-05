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

largura_grafico = largura_janela * 0.75
altura_grafico = altura_janela * 0.85
figura = Figure(figsize=(largura_grafico / DPI, altura_grafico / DPI), dpi=DPI)
figura.patch.set_facecolor("#cfcfcf")
graficos = figura.subplots(2)

canvas = FigureCanvasTkAgg(figura, janela_principal)
canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


variacao = 1
indice = np.arange(variacao)
largura_barra = 0.1
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
    color="#000",
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
    color="#cecece",
    label=f"Total: {media_lucro}",
)

graficos[1].plot(
    range(1000),
    lucros,
    color="#c91509",
    label="Média",
)

# graficos[0].set_xlim(0,100)
graficos[0].set_ylim(0, 12)
graficos[0].set_xlim(0, 1)
graficos[0].set_title("Probabilidades de Ocorrência", fontweight="bold")
graficos[0].set_xticks(indice + largura_barra)
graficos[0].legend()
graficos[0].grid(True)


graficos[1].set_title("Variação de saldo", fontweight="bold")
graficos[1].grid(True)


def set_valor_inicial(event):
    print("FDC!")


def set_valor_variacao(event):
    print("FDC!")


def set_valor_multiplo(event):
    print("FDC!")


# Label do valor inicial
Label(
    janela_principal, text="Valor Inicial:", bg="#cfcfcf", fg="#000", font=13, anchor=W
).place(relx=0.82, rely=0.25, anchor=tk.CENTER)
valor_inicial = tk.Entry(janela_principal)
valor_inicial.bind("<Return>", set_valor_inicial)
valor_inicial.place(relx=0.82, rely=0.28, anchor=tk.CENTER)

# Label do valor de variação
Label(
    janela_principal,
    text="Valor de Variação:",
    bg="#cfcfcf",
    fg="#000",
    font=13,
    anchor=W,
).place(relx=0.82, rely=0.36, anchor=tk.CENTER)
valor_variacao = tk.Entry(janela_principal)
valor_variacao.bind("<Return>", set_valor_variacao)
valor_variacao.place(relx=0.82, rely=0.39, anchor=tk.CENTER)

# Label do valor multiplo que irá variar
Label(
    janela_principal,
    text="Multiplo da Variação:",
    bg="#cfcfcf",
    fg="#000",
    font=13,
    anchor=W,
).place(relx=0.82, rely=0.47, anchor=tk.CENTER)
valor_multiplo = tk.Entry(janela_principal)
valor_multiplo.bind("<Return>", set_valor_multiplo)
valor_multiplo.place(relx=0.82, rely=0.50, anchor=tk.CENTER)

# Footer
# Label(janela_principal, text="Desenvolvido pelos discentes de Eng. da Computação - 2017", bg="#cfcfcf",fg="#000", font=('Helvetica', 18, 'bold'), anchor=W).place(x=180,y=640,width=1080, height=27)
# Label(janela_principal, text="Allef Fonseca - Bryan Franklin Sena - João Vitor Farias - Kristhyan Maia - Mario Victor Silva - Mikael Almondes", bg="#cfcfcf",fg="#000", font=('Helvetica', 11), anchor=W).place(x=175,y=670,width=1080, height=20)

janela_principal.mainloop()
