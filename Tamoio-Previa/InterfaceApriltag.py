import tkinter as tk
import os
from tkinter import filedialog, messagebox
from ReconhecedorImagemApriltag import ReconhecedorImagemApriltag

class Interface:

    def __init__(self, root):
        self.root = root
        self.root.title('Tamoio')
        self.root.resizable(False, False)

        self.arquivosGerados = 0
        self.arquivosTotais = 0

        # Folha do Caderno
        self.textoFolhaCaderno = tk.Label(root, text='Folha do Caderno:')
        self.textoFolhaCaderno.grid(row=0, column=0, padx=10, pady=5)
        self.caminhoFolhaCaderno = tk.Entry(root, width=50)
        self.caminhoFolhaCaderno.grid(row=0, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoFolhaCaderno = tk.Button(root, text='Selecionar', command=self.selecionarCaminhoFolhaCaderno)
        self.botaoSelecionarCaminhoFolhaCaderno.grid(row=0, column=2, padx=10, pady=5)

        # Marcação 1
        self.textoMarcacao1 = tk.Label(root, text='Marcação 1:')
        self.textoMarcacao1.grid(row=1, column=0, padx=10, pady=5)
        self.caminhoMarcacao1 = tk.Entry(root, width=50)
        self.caminhoMarcacao1.grid(row=1, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoMarcacao1 = tk.Button(root, text='Selecionar', command=self.selecionarMarcacao1)
        self.botaoSelecionarCaminhoMarcacao1.grid(row=1, column=2, padx=10, pady=5)

        # Marcação 2
        self.textoMarcacao2 = tk.Label(root, text='Marcação 2:')
        self.textoMarcacao2.grid(row=2, column=0, padx=10, pady=5)
        self.caminhoMarcacao2 = tk.Entry(root, width=50)
        self.caminhoMarcacao2.grid(row=2, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoMarcacao2 = tk.Button(root, text='Selecionar', command=self.selecionarMarcacao2)
        self.botaoSelecionarCaminhoMarcacao2.grid(row=2, column=2, padx=10, pady=5)

        # Marcação 3
        self.textoMarcacao3 = tk.Label(root, text='Marcação 3:')
        self.textoMarcacao3.grid(row=3, column=0, padx=10, pady=5)
        self.caminhoMarcacao3 = tk.Entry(root, width=50)
        self.caminhoMarcacao3.grid(row=3, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoMarcacao3 = tk.Button(root, text='Selecionar', command=self.selecionarMarcacao3)
        self.botaoSelecionarCaminhoMarcacao3.grid(row=3, column=2, padx=10, pady=5)

        # Marcação 4
        self.textoMarcacao4 = tk.Label(root, text='Marcação 4:')
        self.textoMarcacao4.grid(row=4, column=0, padx=10, pady=5)
        self.caminhoMarcacao4 = tk.Entry(root, width=50)
        self.caminhoMarcacao4.grid(row=4, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoMarcacao4 = tk.Button(root, text='Selecionar', command=self.selecionarMarcacao4)
        self.botaoSelecionarCaminhoMarcacao4.grid(row=4, column=2, padx=10, pady=5)

        # Resultado
        self.textoResultado = tk.Label(root, text='Salvar em:')
        self.textoResultado.grid(row=5, column=0, padx=10, pady=5)
        self.caminhoResultado = tk.Entry(root, width=50)
        self.caminhoResultado.grid(row=5, column=1, padx=10, pady=5)
        self.botaoSelecionarCaminhoResultado = tk.Button(root, text='Selecionar', command=self.selecionarResultado)
        self.botaoSelecionarCaminhoResultado.grid(row=5, column=2, padx=10, pady=5)

        # Botão Resultado
        self.botaoResultado = tk.Button(root, text='Gerar Resultado', command=self.gerarResultado)
        self.botaoResultado.grid(row=6, columnspan=3, padx=10, pady=10)

        # Barra de progresso
        self.progresso = tk.Label(root, text="Arquivos gerados: 0")
        self.progresso.grid(row=7, columnspan=3, padx=10, pady=5)

    def atualizarProgresso(self):
        self.progresso.config(text=f"Arquivos gerados: {self.arquivosGerados} de {self.arquivosTotais}")

    def selecionarCaminhoFolhaCaderno(self):
        caminhosFolhaCadernoSelecionados = filedialog.askopenfilenames(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoFolhaCaderno.delete(0, tk.END)
        for caminho in caminhosFolhaCadernoSelecionados:
            self.caminhoFolhaCaderno.insert(tk.END, caminho + '\n')

    def selecionarMarcacao1(self):
        caminhoMarcacao1Selecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao1.delete(0, tk.END)
        self.caminhoMarcacao1.insert(tk.END, caminhoMarcacao1Selecionado)

    def selecionarMarcacao2(self):
        caminhoMarcacao2Selecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao2.delete(0, tk.END)
        self.caminhoMarcacao2.insert(tk.END, caminhoMarcacao2Selecionado)

    def selecionarMarcacao3(self):
        caminhoMarcacao3Selecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao3.delete(0, tk.END)
        self.caminhoMarcacao3.insert(tk.END, caminhoMarcacao3Selecionado)

    def selecionarMarcacao4(self):
        caminhoMarcacao4Selecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao4.delete(0, tk.END)
        self.caminhoMarcacao4.insert(tk.END, caminhoMarcacao4Selecionado)

    def selecionarMarcacao2(self):
        caminhoMarcacao2Selecionado = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg')])
        self.caminhoMarcacao2.delete(0, tk.END)
        self.caminhoMarcacao2.insert(tk.END, caminhoMarcacao2Selecionado)

    def selecionarResultado(self):
        caminhoResultadoSelecionado = filedialog.askdirectory()
        self.caminhoResultado.delete(0, tk.END)
        self.caminhoResultado.insert(tk.END, caminhoResultadoSelecionado)

    def gerarResultado(self):
        self.arquivosGerados = 0
        self.atualizarProgresso()

        folhasCaderno = self.caminhoFolhaCaderno.get().split('\n')
        self.arquivosTotais = len(folhasCaderno)-1
        marcacao1 = self.caminhoMarcacao1.get()
        marcacao2 = self.caminhoMarcacao2.get()
        marcacao3 = self.caminhoMarcacao3.get()
        marcacao4 = self.caminhoMarcacao4.get()
        resultado = self.caminhoResultado.get()

        if folhasCaderno and marcacao1 and marcacao2 and marcacao3 and marcacao4 and resultado:
            for folhaCaderno in folhasCaderno:
                if folhaCaderno:
                    try:
                        reconhecedorImagemApriltag = ReconhecedorImagemApriltag(folhaCaderno, marcacao1, marcacao2,
                                                                                marcacao3, marcacao4, resultado)

                        self.arquivosGerados += 1
                        self.atualizarProgresso()

                        messagebox.showinfo("Sucesso", f"Resultado de {str( os.path.basename(folhaCaderno) )} gerado com sucesso!")
                    except Exception as e:
                        messagebox.showerror("Erro", f"Erro na geração do arquivo: {str(e)}")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

root = tk.Tk()
interface = Interface(root)
root.mainloop()
