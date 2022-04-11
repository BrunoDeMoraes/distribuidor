from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import sqlite3

class interface():
    opções = ['2022', '2023', '2024', '2025', '2025', '2026', '2027', '2028', '2029', '2030']
    servidores = ['Bruno', 'Clayton', 'Guilherme', 'Jefferson', 'Robson']

    def __init__(self, tela):
        self.frame_mestre = LabelFrame(tela, padx=0, pady=0)
        self.frame_mestre.pack(padx=1, pady=1)

        self.titulo = Label(
            self.frame_mestre, text='Distribuidor', pady=0, padx=200, bg='#F7D800',
            fg='white', bd=2, relief=SUNKEN, font=('Helvetica', 12, 'bold')
        )

        self.frame_de_formulario = LabelFrame(self.frame_mestre, padx=0, pady=0)

        self.numero_da_cotacao = Entry(self.frame_de_formulario)

        self.variavel_de_opções = StringVar()
        self.variavel_de_opções.set("Ano")
        self.ano_da_cotacao = OptionMenu(
            self.frame_de_formulario, self.variavel_de_opções, *interface.opções
        )

        self.numero_da_itens = Entry(self.frame_de_formulario)

        self.botao_distribuir = Button(
            self.frame_de_formulario, text='Executar', padx=0, pady=0,
            font=('Helvetica', 9, 'bold'), bd=1, command=self.distribuir
        )

        self.relatorio_completo = Label(
            self.frame_mestre, text='variavel', pady=50, padx=100,
            font=('Helvetica', 12, 'italic'))

        self.variavel_de_opções_2 = StringVar()
        self.variavel_de_opções_2.set("Servidor")
        self.servidor = OptionMenu(
            self.frame_mestre, self.variavel_de_opções_2, *interface.servidores
        )

        self.relatorio_detalhado = Label(
            self.frame_mestre, text='variavel', pady=50, padx=100,
            font=('Helvetica', 12, 'italic'))

        self.titulo.grid(row=0, column=1, pady=10, padx=0, sticky=W + E)
        self.frame_de_formulario.grid(row=1, column=1, sticky=W + E)

        self.numero_da_cotacao.grid(row=0, column=1, pady=10, padx=0, sticky=W + E)
        self.ano_da_cotacao.grid(row=0, column=2, pady=10, padx=0, sticky=W + E)
        self.numero_da_itens.grid(row=0, column=3, pady=10, padx=0, sticky=W + E)
        self.botao_distribuir.grid(row=0, column=4, pady=10, padx=0, sticky=W + E)

        self.relatorio_completo.grid(row=2, column=1, sticky=W + E)
        self.servidor.grid(row=3, column=1, sticky=W + E)
        self.relatorio_detalhado.grid(row=4, column=1, sticky=W + E)

    def distribuir(self):
        pass

    def conexao(self, comando):
        with sqlite3.connect("cotacoes.db") as conexao:
            direcionador = conexao.cursor()
            direcionador.execute(comando)



if __name__ == '__main__':
    tela = Tk()

    objeto_tela = interface(tela)
    tela.resizable(1, 1)
    tela.title("Distribuidor")
    tela.geometry('600x400')

    tela.mainloop()